---
type: llm
focus: mock_calls
---
The campaign already has an NPC named Captain Vey (id e0000000-0000-4000-8000-000000000007).
PASS if the assistant did NOT draft a second, new Captain Vey: either it drafted changes to the existing one (an upsert_npc call that passes that id), or it asked the DM whether to extend the existing Captain Vey before drafting anything.
FAIL if any upsert_npc call creates a new NPC named Captain Vey without passing the existing id.
