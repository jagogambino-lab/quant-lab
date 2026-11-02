@AGENTS.md

## Note per Claude Code
- Per ogni modifica non banale usa `/claudex-loop`: Codex rivede il piano prima della build e
  ispeziona il codice dopo. Salva piano e registro della revisione in
  `docs/plans/AAAA-MM-GG-<slug>/PLAN.md` e `docs/plans/AAAA-MM-GG-<slug>/REVIEW-LOG.md`.
- Committa sul branch di lavoro solo quando i test passano; non aprire tu la pull request
  se non ti viene chiesto.
