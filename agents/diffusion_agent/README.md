# Emerging Technology Diffusion Agent

Version 0.2-student, revised 2026-10-22 for Assignment 5. Status: v0.1 executions validated and evaluated; v0.2 implementation locally verified only, with model retesting pending.

## Purpose and evidence

Analyze GenAI diffusion for human-reviewed internal service-desk incident documentation. Preserve general, application and organization findings; all five Rogers factors; evidence uncertainty; and the Diffusion/Adoption boundary. The two organizations are hypothetical. ITSM is a function, not an assumed industry. The fixed source register is embedded verbatim in both cases' additional_context. Original URLs, dates, definitions and source limitations are in records/evidence_register.md. No external API or new dependency is required.

## Reproduce preparation from the scaffold root

Use the unchanged tools/build_prompt.py with --agent agents/diffusion_agent and --case agents/diffusion_agent/cases/primary.json, adding --out agents/diffusion_agent/records/primary_v02_prompt.txt. Repeat for contrast_1.json and records/contrast_1_v02_prompt.txt. This override keeps reviewable packets within the student-agent folder rather than ignored work/.

After explicit v0.2 execution approval, submit each packet to ChatGPT and save the returned JSON in responses/ with versioned filenames. Then run the unchanged tools/validate_response.py on each response. Also inspect full schema conformance, facts, category support and contextual sensitivity; basic validator success alone is insufficient. Preserve the input and instruction version for every output. Do not overwrite a weak result.

## Evaluation history and pending comparison

The original v0.1 responses, official validation logs and Phase 3 evaluation are preserved. After approval, run primary and contrast at v0.2 and compare against v0.1. Expect stable general/application evidence and potentially different organization-specific timing and prerequisites. Posture and governance vary jointly, so do not infer a posture-only causal effect. Find and preserve a genuine weakness, decide a bounded revision, and rerun the same inputs. Optional same-case repeat, wording variant or W1 challenge only within the course time budget. Do not manufacture a failed run. Record outcomes in records/test_record.md. Phase 2 did not evaluate the model; Phase 3 evaluated the supplied v0.1 outputs. v0.2 model evaluation remains pending.

## Known limitations

Selective public evidence; no representative application-specific penetration sample; undated vendor customer report; older GenAI survey; broader AI evidence has a different definition and population; adjacent cloud prototype is not internal ITSM adoption. Local performance, permission, integration and reviewer readiness remain unknown. Evidence-based self-critique is prompt-based; known W1 handling was observed in v0.1, but novel error detection and v0.2 effectiveness remain unproven. It cannot guarantee accuracy. Exact Rogers categories may require abstention. Review original sources before later consequential use, version any refreshed evidence, and keep both comparison packets synchronized.

## Record and handoff

The preserved blank Template (8) in records/ is authoritative for Sections A-F. agent_record.md is an unfilled field map, not a final record. Agent self-critique and personal Section F reflection are separate. Development decisions must distinguish user instructions from assistant implementation choices. GitHub operations belong exclusively to the student. Do not edit frozen core, tools, templates or schemas. Stop at 90 minutes of focused assignment effort and preserve unresolved work.

## Phase 4 records

records/v01/ preserves the original instructions, metadata and Phase 2 README/test plan. The existing primary_prompt.txt and contrast_1_prompt.txt remain the original v0.1 packets. New *_v02_prompt.txt packets contain v0.2 instructions with unchanged cases/evidence. See phase4_revision_map.md, phase4_implementation_report.md and v01_to_v02_instructions.diff. section_f_provisional.md is a companion working reflection for student confirmation; the original Word Template (8) and Agent Record fields remain unfilled. Historical Phase 2/3 reports are not current-version status documents.
