# Aim

Aim is a personal planning system that turns goals into actions.

> A system for figuring out what to do next.

Calendars tell you **when**.

Task managers tell you **what**.

Aim tries to answer:

> What should I do with my time?

Aim considers your goals, deadlines, available time, previous execution, and current tasks to determine what deserves your time.It doesn't just make plans. It learns from what actually happens and uses that experience to improve the next one.

If plans consistently fail, Aim adapts. If a goal falls behind, Aim warns you.

It sits above your existing calendar and task manager rather than replacing them.

### Architecture

```text
                    Aim
                     │
       ┌─────────────┼─────────────┐
       ↓             ↓             ↓
    Memory           AI         Planner
       │                           │
       │                  ┌────────┴────────┐
       │                  ↓                 ↓
       │              Planning         Scheduling
       │
       └────────────── personal state
                              │
                 ┌────────────┴────────────┐
                 ↓                         ↓
          Google Tasks             Google Calendar
```

- **Memory** remembers.

- **AI** interprets.

- **Planner** decides.

- **Scheduler** finds time.

- **Calendar and Tasks** hold the resulting work.

### Principles

* Local-first
* Human in loop
* Structured memory
* Deterministic planning where possible
* LLMs for interpretation, not authority
* Use existing tools instead of rebuilding them

Early development. Built for personal use.