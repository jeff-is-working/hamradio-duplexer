"""Tests for tools/validate_inventory.py - written test-first (TDD).

Run: pytest -q
"""

import textwrap
from pathlib import Path

import pytest

from tools.validate_inventory import ValidationError, validate_unit, BANDS


def _write(tmp_path: Path, body: str) -> Path:
    p = tmp_path / "unit.yaml"
    p.write_text(textwrap.dedent(body).lstrip(), encoding="utf-8")
    return p


# --- happy paths ----------------------------------------------------------

def test_valid_2m_planned_unit_passes(tmp_path):
    p = _write(tmp_path, """
        id: t1480-4cav-a
        model: T1480
        band: 2m
        cavities: 4
        cable_state: intact
        rx_freq_mhz: 145.150
        tx_freq_mhz: 145.750
        ctcss_hz: 100.0
        status: planned
    """)
    unit = validate_unit(p)
    assert unit["id"] == "t1480-4cav-a"


def test_valid_commissioned_requires_measurements_passes(tmp_path):
    p = _write(tmp_path, """
        id: gmrs-uhf-1
        model: T1504
        band: gmrs
        cavities: 4
        cable_state: intact
        rx_freq_mhz: 467.550
        tx_freq_mhz: 462.550
        status: commissioned
        insertion_loss_db: 1.4
        isolation_db: 82
    """)
    unit = validate_unit(p)
    assert unit["status"] == "commissioned"


# --- required fields / structure -----------------------------------------

def test_missing_required_field_fails(tmp_path):
    p = _write(tmp_path, """
        id: broken
        band: 2m
        cavities: 2
        rx_freq_mhz: 145.150
        tx_freq_mhz: 145.750
        status: planned
    """)  # no model, no cable_state
    with pytest.raises(ValidationError):
        validate_unit(p)


def test_unknown_band_fails(tmp_path):
    p = _write(tmp_path, """
        id: x
        model: T9999
        band: 900mhz
        cavities: 2
        cable_state: cut
        rx_freq_mhz: 906.0
        tx_freq_mhz: 919.0
        status: planned
    """)
    with pytest.raises(ValidationError):
        validate_unit(p)


# --- band / frequency sanity ---------------------------------------------

def test_freq_out_of_band_fails(tmp_path):
    # 2m band is 144-148; rx at 220 is not in band
    p = _write(tmp_path, """
        id: oob
        model: T1480
        band: 2m
        cavities: 4
        cable_state: intact
        rx_freq_mhz: 220.150
        tx_freq_mhz: 145.750
        status: planned
    """)
    with pytest.raises(ValidationError):
        validate_unit(p)


def test_vhf_model_on_uhf_band_fails(tmp_path):
    # T1480 series is VHF-only; declaring it on a UHF band is an error
    p = _write(tmp_path, """
        id: mismatch
        model: T1480
        band: 70cm
        cavities: 4
        cable_state: intact
        rx_freq_mhz: 449.150
        tx_freq_mhz: 444.150
        status: planned
    """)
    with pytest.raises(ValidationError):
        validate_unit(p)


def test_uhf_t1500_on_2m_band_fails(tmp_path):
    # T1500 series is UHF-only; declaring it on 2m is an error
    p = _write(tmp_path, """
        id: mismatch2
        model: T1500
        band: 2m
        cavities: 4
        cable_state: intact
        rx_freq_mhz: 145.150
        tx_freq_mhz: 145.750
        status: planned
    """)
    with pytest.raises(ValidationError):
        validate_unit(p)


def test_split_too_small_for_band_fails(tmp_path):
    # GMRS split must be ~5 MHz; 100 kHz is implausible / typo guard
    p = _write(tmp_path, """
        id: badsplit
        model: T1504
        band: gmrs
        cavities: 4
        cable_state: intact
        rx_freq_mhz: 462.650
        tx_freq_mhz: 462.550
        status: planned
    """)
    with pytest.raises(ValidationError):
        validate_unit(p)


# --- commissioning gate ---------------------------------------------------

def test_commissioned_without_measurements_fails(tmp_path):
    p = _write(tmp_path, """
        id: notdone
        model: T1480
        band: 2m
        cavities: 4
        cable_state: intact
        rx_freq_mhz: 145.150
        tx_freq_mhz: 145.750
        status: commissioned
    """)
    with pytest.raises(ValidationError):
        validate_unit(p)


def test_cavities_must_be_positive_int(tmp_path):
    p = _write(tmp_path, """
        id: zerocav
        model: T1480
        band: 2m
        cavities: 0
        cable_state: intact
        rx_freq_mhz: 145.150
        tx_freq_mhz: 145.750
        status: planned
    """)
    with pytest.raises(ValidationError):
        validate_unit(p)


def test_bands_table_has_expected_bands():
    assert {"2m", "70cm", "gmrs"} <= set(BANDS)
