# Evals

`claude plugin eval` cases for the questmaster-vtt plugin. Every case runs against
the mocks in `mocks/questmaster-vtt/` (a fictional campaign, "The Ashfall Reach"),
never against a real QuestMaster account. Run from the plugin folder:

    claude plugin eval . --no-publish --runs 1        # a quick pass
    claude plugin eval . --no-publish                 # 3 runs per arm, with a no-plugin baseline

Cases override suite mocks with their own `mocks/` folder.
