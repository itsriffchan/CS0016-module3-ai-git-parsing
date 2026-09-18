# AI Usage and Validation Log

Student name: Reese Lauren C. Chan

Section: TS31

AI tool used: ChatGPT

## Entry 1 - XML parsing

**Prompt:**
```
I am completing an authorized classroom Python lab.
 Review this function stub and the supplied fictional [XML/JSON/YAML] structure.
 Recommend an implementation that returns exactly the keys described in the docstring.
 Explain namespace handling, data types, error risks, and each library function used.
 Do not invent files, credentials, network calls, or expected test results.
 I will validate your recommendation using unit tests and Git diffs.
 
 Function stub: 
  def parse_xml(path: str | Path) -> dict:
      """Return default_operation and test_option from the NETCONF-style XML."""
      # TODO: parse the XML, handle its default namespace, and return two strings.
      raise NotImplementedError("Complete parse_xml")
 Relevant fictional data: 
  <?xml version="1.0" encoding="UTF-8"?>
  <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <edit-config>
      <target>
        <candidate />
      </target>
      <default-operation>merge</default-operation>
      <test-option>test-then-set</test-option>
      <config>
        <interface xmlns="urn:example:network">
          <name>GigabitEthernet1</name>
          <enabled>true</enabled>
        </interface>
      </config>
    </edit-config>
  </rpc>
```

**AI recommendation summary:** The AI recommended to handle the XML namespace using the ElementTree library (which is also aligned with what is required for the assessment). Assign the namespace to the variable `nc`, and pass use that variable to locate the `default_operation` and `test_option strings`.

**Decision:** accepted

**Validation evidence:** The AI suggestion align with the documentation string, correctly handling the namespace and retrieving the necessary variable values.

## Entry 2 - JSON parsing

```
I am completing an authorized classroom Python lab.
 Review this function stub and the supplied fictional [XML/JSON/YAML] structure.
 Recommend an implementation that returns exactly the keys described in the docstring.
 Explain namespace handling, data types, error risks, and each library function used.
 Do not invent files, credentials, network calls, or expected test results.
 I will validate your recommendation using unit tests and Git diffs.
 
 Function stub: 
  def parse_json(path: str | Path) -> dict:
      """Return site, device_count, enabled_devices, and roles from the JSON."""
      # TODO: use json.load and derive the requested summary values.
      raise NotImplementedError("Complete parse_json")

 Relevant fictional data: 
  {
    "site": "FEU-Tech-Lab",
    "devices": [
      {
        "hostname": "R1",
        "management_ip": "192.0.2.10",
        "role": "router",
        "enabled": true
      },
      {
        "hostname": "SW1",
        "management_ip": "192.0.2.20",
        "role": "switch",
        "enabled": true
      },
      {
        "hostname": "AP1",
        "management_ip": "192.0.2.30",
        "role": "wireless-ap",
        "enabled": false
      }
    ]
  }
 ```
**AI recommendation summary:** The AI recommended opening and loading the JSON file in read mode, then extracting the required values using their respective keys.

**Decision:** Accepted. 

**Validation evidence:** The solution aligns with what the docstring requires and stores the necessary values in an appropriate data type (int, list, etc.)

## Entry 3 - YAML parsing and integration

**Prompt:**

**AI recommendation summary:**

**Decision:** accepted / modified / rejected

**Validation evidence:**

## Controlled merge-conflict line

Validation status: PENDING

## Final reflection

Describe one AI suggestion that you changed or rejected and explain the evidence that guided your decision.
