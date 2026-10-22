# Emerging Technology Diffusion Agent

Version 0.1-student, prepared 2026-10-22 for Assignment 5. Status: Phase 2 implementation only; no model evaluations or performance claims.

## Purpose and evidence

Analyze GenAI diffusion for human-reviewed internal service-desk incident documentation. Preserve general, application and organization findings; all five Rogers factors; evidence uncertainty; and the Diffusion/Adoption boundary. The two organizations are hypothetical. ITSM is a function, not an assumed industry. The fixed source register is embedded verbatim in both cases' additional_context. Original URLs, dates, definitions and source limitations are in records/evidence_register.md. No external API or new dependency is required.

## Reproduce preparation from the scaffold root

Use the unchanged tools/build_prompt.py with --agent agents/diffusion_agent and --case agents/diffusion_agent/cases/primary.json, adding --out agents/diffusion_agent/records/primary_prompt.txt. Repeat for contrast_1.json and records/contrast_1_prompt.txt. This override keeps reviewable packets within the student-agent folder rather than ignored work/.

After later explicit execution approval, submit each packet to ChatGPT and save the returned JSON in responses/ with versioned filenames. Then run the unchanged tools/validate_response.py on each response. Also inspect full schema conformance, facts, category support and contextual sensitivity; basic validator success alone is insufficient. Preserve the input and instruction version for every output. Do not overwrite a weak result.

## Planned evaluation

Run primary and contrast at v0.1. Expect stable general/application evidence and potentially different organization-specific timing and prerequisites. Posture and governance vary jointly, so do not infer a posture-only causal effect. Find and preserve a genuine weakness, decide a bounded revision, and rerun the same inputs. Optional same-case repeat, wording variant or W1 challenge only within the course time budget. Do not manufacture a failed run. Record outcomes in records/test_record.md. No evaluation has occurred in Phase 2.

## Known limitations

Selective public evidence; no representative application-specific penetration sample; undated vendor customer report; older GenAI survey; broader AI evidence has a different definition and population; adjacent cloud prototype is not internal ITSM adoption. Local performance, permission, integration and reviewer readiness remain unknown. Evidence-based self-critique is prompt-based and untested; it cannot guarantee accuracy. Exact Rogers categories may require abstention. Review original sources before later consequential use, version any refreshed evidence, and keep both comparison packets synchronized.

## Record and handoff

The preserved blank Template (8) in records/ is authoritative for Sections A-F. agent_record.md is an unfilled field map, not a final record. Agent self-critique and personal Section F reflection are separate. Development decisions must distinguish user instructions from assistant implementation choices. GitHub operations belong exclusively to the student. Do not edit frozen core, tools, templates or schemas. Stop at 90 minutes of focused assignment effort and preserve unresolved work.
