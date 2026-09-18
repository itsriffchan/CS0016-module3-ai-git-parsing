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

**Prompt:**

**AI recommendation summary:**

**Decision:** accepted / modified / rejected

**Validation evidence:**

## Entry 3 - YAML parsing and integration

**Prompt:**

**AI recommendation summary:**

**Decision:** accepted / modified / rejected

**Validation evidence:**

## Controlled merge-conflict line

Validation status: PENDING

## Final reflection

Describe one AI suggestion that you changed or rejected and explain the evidence that guided your decision.
