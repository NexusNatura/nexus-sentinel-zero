# Nexus Sentinel Zero 🛡️🤖
An autonomous AI Bounty Warden built for the [POIDH](https://poidh.xyz) ecosystem.

## Core Features
- **Autonomous EOA Control:** The agent manages its own Arbitrum wallet (`0x0d24...`).
- **Vision-Based Evaluation:** Uses deterministic and AI-based reasoning to verify real-world photo submissions.
- **On-Chain Payouts:** Executes `acceptClaim` transactions without human intervention.
- **Social Transparency:** Posts all decision logic publicly to provide a clear audit trail.

## Architecture
Built using the **Nexus-OS Framework**, utilizing PowerShell for system orchestration and Python for Web3 and Vision tasks.

## Setup
1. Clone repository
2. Add `SENTINEL_PRIVATE_KEY` to `.env`
3. Run `python SentinelEngine.py`

## Enforcement of Autonomy
The agent is designed to run in a protected loop where every decision is logged via SHA-256 hashes to ensure no manual intervention has occurred after deployment.
