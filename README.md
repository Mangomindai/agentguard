# AgentGuard

**AI Agent Governance Kernel — Trust, Approvals, Audit**

If your agent can break this — 
it better be good at breaking Bitcoin.

> *"Your AI agents are only as safe as the system governing them."*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)

---

## The Problem

You're building with AI agents. Your agent has access to your database, your payments, your users.

**What happens when it does something it shouldn't?**

Most startups have no answer. No pause button. No audit trail. No trust scoring. No approval gate. Just an agent with full access and a prayer.

AgentGuard changes that.

---

## What AgentGuard Does

```
Agent wants to take an action
              ↓
AgentGuard checks:
  → Is this agent trusted enough?
  → Is this action too risky?
  → Does a human need to approve this?
  → Is this agent even allowed to act right now?
              ↓
ALLOW    → action proceeds, logged
PENDING  → paused, human notified for approval
BLOCK    → stopped, agent trust score drops
AUTO-BLOCK → agent trust too low, fully quarantined
```

Every decision is logged. Every action is auditable. Every agent is revocable.

---

## Core Features

**Trust Engine**
Every agent has a trust score (0.0 → 1.0). Successful actions build trust. Failures reduce it. Drop below 0.3 and the agent is automatically blocked. No human needed.

```
TRUSTED → LIMITED → OBSERVED → SUSPICIOUS → QUARANTINED → REVOKED
```

**Capability Tokens**
Agents get scoped, time-limited, cryptographically signed tokens. Not broad API keys. Specific permissions for specific resources that expire automatically.

**Human-in-the-Loop Approval Gate**
Risky actions (delete, transfer, export) pause automatically and wait for a human to approve or deny. Your on-call engineer gets notified. The agent waits.

**Risk Engine**
Every action is scored 0–100 based on action type, resource sensitivity, and time of day. High risk = approval required. Critical risk = hard stop.

**Real-time Event Stream**
SSE endpoint streams every agent event to your dashboard in real time. See trust changes, approvals, blocks as they happen.

**Full Audit Trail**
Every action, every decision, every trust change — immutably logged with actor, timestamp, policy version, and outcome. Your enterprise clients will stop asking uncomfortable questions.

---

## Quick Start

```bash
pip install agentguard
```

```python
from agentguard import TrustEngine

engine = TrustEngine(db_path="trust.db")

# New agent starts TRUSTED
level = engine.get_trust_level("my-agent-001")
print(level)  # → TRUSTED

# Agent does something bad
result = engine.apply_penalty("my-agent-001", "spam")
print(result)  # → {"new_points": 20, "new_level": "LIMITED"}

# Agent does something bad again
result = engine.apply_penalty("my-agent-001", "abuse")
print(result)  # → {"new_points": 50, "new_level": "OBSERVED"}

# Agent recovers with good behaviour
engine.upgrade_trust("my-agent-001", reason="passed_review")

# Get full history
history = engine.get_history("my-agent-001")
```

---

## Trust Engine (kernel.py)

The trust engine is a standalone module — use it without the full API if you prefer.

```python
from agentguard import TrustEngine

engine = TrustEngine(db_path="trust.db")

# Check trust level
level = engine.get_trust_level("agent-123")
# → "TRUSTED" | "LIMITED" | "OBSERVED" | "SUSPICIOUS" | "QUARANTINED" | "REVOKED"

# Apply a violation
result = engine.apply_penalty("agent-123", "unauthorized_access")
# → {"new_points": 40, "new_level": "OBSERVED"}

# Reward good behaviour
engine.upgrade_trust("agent-123", reason="successful_completion")

# Agent appeals a block
engine.submit_appeal("agent-123",
    reason="False positive",
    evidence="Logs show normal behaviour")

# Get history
history = engine.get_history("agent-123")
```

### Trust Levels

| Level | Points | What it means |
|-------|--------|---------------|
| TRUSTED | 0–19 | Full access, normal operation |
| LIMITED | 20–39 | Restricted actions, monitored |
| OBSERVED | 40–59 | All actions logged, some blocked |
| SUSPICIOUS | 60–79 | Most actions require approval |
| QUARANTINED | 80–99 | Almost fully restricted |
| REVOKED | 100 | Completely blocked |

### Violation Penalties

| Violation | Points |
|-----------|--------|
| fake_verification | 50 |
| hate_speech | 60 |
| drug_listing | 40 |
| high_risk_activity | 35 |
| abuse | 30 |
| multiple_flags | 25 |
| spam | 20 |

---

## Architecture

```
┌─────────────────────────────────────────────────┐
│                   Your App                       │
├─────────────────────────────────────────────────┤
│         AgentGuard Kernel (kernel.py)            │
│    Trust Engine │ Risk Scoring │ Audit Log       │
├─────────────────────────────────────────────────┤
│              SQLite (default)                    │
│         PostgreSQL (Enterprise)                  │
└─────────────────────────────────────────────────┘
```

`kernel.py` — pure trust logic, no dependencies, drop into any project in 5 minutes.

Full REST API with approval gates, capability tokens, and real-time monitoring available in Enterprise Edition.

---

## Community vs Enterprise

| Feature | Community | Enterprise |
|---------|-----------|------------|
| Trust Engine | ✅ Free | ✅ |
| Violation tracking | ✅ Free | ✅ |
| Appeals system | ✅ Free | ✅ |
| REST API | ❌ | ✅ |
| Capability tokens | ❌ | ✅ |
| Approval gate | ❌ | ✅ |
| Dashboard UI | ❌ | ✅ |
| SSO / SAML | ❌ | ✅ |
| SLA | ❌ | ✅ |
| Support | Community | Priority |
| Price | Free | Contact |

---

## Full API — Enterprise Edition

The complete REST API includes:

- JWT authentication
- Capability tokens (scoped, time-limited, cryptographically signed)
- Human approval gate (risky actions pause for human review)
- Real-time SSE event stream
- Risk engine (0–100 scoring per action)
- Full immutable audit trail
- Agent supervision (pause, resume, block, global pause)
- Multi-tenant organisations
- PostgreSQL + Redis for production scale

📧 Contact for Enterprise access and pricing.

---

## Why AgentGuard

| | AgentGuard | DIY | Other tools |
|---|---|---|---|
| Trust decay | ✅ | Build it | ❌ |
| Capability tokens | ✅ | Build it | ❌ |
| Human approval gate | ✅ | Build it | Partial |
| Real-time event stream | ✅ | Build it | ❌ |
| Audit trail | ✅ | Build it | Partial |
| Drop-in kernel | ✅ | — | ❌ |
| Open source | ✅ | — | ❌ |
| Setup time | 5 min | Weeks | Days |

---

## Roadmap

- [ ] pip installable package (`pip install agentguard`)
- [ ] Dashboard UI
- [ ] Webhook notifications (Slack, email)
- [ ] Multi-tenant organisations
- [ ] OpenTelemetry integration
- [ ] LangChain / CrewAI native middleware

---

## Contributing

PRs welcome. Open an issue first for major changes.

---

## Licence

MIT — free to use, modify, and build on. See [LICENSE](LICENSE).

---

## Contact

**Dheeraj Kumar Biswakarma**
📧 bkdk62309@gmail.com
🐙 github.com/Mangomindai/agentguard

For enterprise enquiries, integration support, or custom features — email directly. Response within 24 hours.

---

## Author

Built while trying to build something else entirely — which is how the best infrastructure gets made.

---

*If AgentGuard saved your team from a 3am incident, give it a ⭐*
