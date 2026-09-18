# AI-Assisted Git Workflow and Python Data Parsing

Student name: Reese Chan

Section: TS31

## Project purpose

> Briefly explain how this repository combines Git version control with XML, JSON, and YAML parsing.

This repository served as the Git version control for the data parsers (XML, JSON, YAML). Each parser was separately built and committed to a dedicated branch, before being merged with the main branch. Subsequently, each parser included its own part in `AI_USAGE_LOG.md`, ensuring that all changes are documented properly and backed by evidence.

## How to run

```bash
python3 parser_template.py
python3 -m unittest -v
```

## Git workflow summary
> List the branches and major commits you created. Explain the controlled merge conflict and its resolution.

List of branches:
* main
* feature/data-parsers
* docs/ai-note

The controlled merge conflict proposed a non-major conflict issue between doc files that had two different statuses. In this case, the resolution was simply choosing which version to retain, and which to discard. 

## Parser results

> Summarize the verified XML, JSON, and YAML values.

The parsers were all built inside a `build_summary` function, which returned the following:
- **XML**: 
    - "default_operation": "merge"
    - "test_option": "test-then-set"
- **JSON**:
    - "site": "FEU-Tech-Lab"
    - "device_count": 3
    - "enabled_devices": ["R1","SW1"]
    -"roles": ["router","switch","wireless-ap"]
- **YAML**: 
    - "name": "Saturday-Lab"
    - "approved": true
    - "duration_minutes": 90
    - "devices": ["R1","SW1"]
    - "action": "validate-configuration"
  
## AI disclosure
> Identify the AI tool used and summarize how you validated, modified, or rejected its recommendations.

The AI tool used was ChatGPT Sol 5.6, to assist in constructing the different parsers as well as building the summary. Each result was independtly verified and tested using the provided `test_parser.py`. A detailed documentation of its use can be found in [AI_USAGE_LOG.md](AI_USAGE_LOG.md)

## Safety statement

> Confirm that only the provided fictional data was used and that no credentials, tokens, private repository data, or personal information were submitted to AI.

No credentials, tokens, private repository data, nor personal information was submitted to the AI. It followed the restrictions set by the prompt, those being the function definition and respective data file only.
