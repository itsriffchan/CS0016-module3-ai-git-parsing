"""Module 3 combined lab starter.

Complete each function with help from an approved AI tool, then verify every
claim and code change using the supplied unit tests. The files contain only
fictional classroom data.
"""

import json
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml


def parse_xml(path: str | Path) -> dict:
    """Return default_operation and test_option from the NETCONF-style XML."""
    tree = ET.parse(path)
    root = tree.getroot()

    ns = {"nc": "urn:ietf:params:xml:ns:netconf:base:1.0"}

    default_operation = root.find(".//nc:default-operation", ns)
    test_option = root.find(".//nc:test-option", ns)

    if default_operation is None or test_option is None:
        raise ValueError("Required NETCONF XML elements are missing")

    return {
        "default_operation": default_operation.text,
        "test_option": test_option.text,
    }


def parse_json(path: str | Path) -> dict:
    """Return site, device_count, enabled_devices, and roles from the JSON."""

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    devices = data["devices"]

    return {
        "site": data["site"],
        "device_count": len(devices),
        "enabled_devices": [device["hostname"] for device in devices if device['enabled']],
        "roles": [device["role"] for device in devices],
    }

def parse_yaml(path: str | Path) -> dict:
    """Return name, approved, duration_minutes, devices, and action from YAML."""

    with open(path, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    window = data["window"]

    return {
        "name": window["name"],
        "approved": window["approved"],
        "duration_minutes": window["duration_minutes"],
        "devices": data["devices"],
        "action": data["action"],
    }


def build_summary(xml_path: str | Path, json_path: str | Path, yaml_path: str | Path) -> dict:
    """Combine the three parser results into one dictionary."""
    return {
        "xml": parse_xml(xml_path),
        "json": parse_json(json_path),
        "yaml": parse_yaml(yaml_path)
    }


if __name__ == "__main__":
    base = Path(__file__).resolve().parent
    summary = build_summary(
        base / "network_config.xml",
        base / "devices.json",
        base / "maintenance.yaml",
    )
    print(json.dumps(summary, indent=2))
