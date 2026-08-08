# SecureApp Pipeline

a**End-to-End DevSecOps Security Across Every Layer of the SDLC**

A deliberately vulnerable Flask application, secured layer by layer through
an 8-stage automated security pipeline — pre-commit scanning, dependency
auditing, CI/CD gating, container hardening, cloud infrastructure security,
dynamic testing, network monitoring, and AI-assisted incident response.
unning blog app homepage. This is the first thing a visitor sees.
-->
<img width="900" height="432" alt="image" src="https://github.com/user-attachments/assets/123ae524-123b-4a62-9b0a-8a1a6756cdc0" />
<img width="1835" height="1016" alt="image" src="https://github.com/user-attachments/assets/b3a8039d-f17f-4dc0-bedc-aec04706cdd0" />

<p align="center">
  <img src="docs/screenshots/01-hero.png" alt="SecureApp Pipeline overview" width="800">
</p>

<p align="center">
  <a href="#"><img lt="Pipeline" src="https://img.shields.io/badge/pipeline-8%20layers-0F1B3C"></a>
  <a href="#"><img alt="Python" src="https://img.shields.io/badge/python-3.12-blue"></a>
  <a href="#"><img alt="License" src="https://img.shields.io/badge/license-MIT-green"></a>
  <a href="#"><img alt="Docker" src="https://img.shields.io/badge/docker-ready-2496ED"></a>
</p>

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [The Vulnerable Application](#the-vulnerable-application)
- [Security Layers](#security-layers)
- [Screenshots](#screenshots)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Documentation](#documentation)
- [Tech Stack](#tech-stack)
- [Future Scope](#future-scope)
- [License](#license)

---

## Overview

Most teams bolt security onto a project right before release. **SecureApp
Pipeline** takes the opposite approach: a real, full-featured Flask
application is built with 12 documented, working vulnerabilities, then
every subsequent layer of the pipeline is built specifically to detect and
block those vulnerabilities — proving each gate actually works rather than
assuming it does.

| | |
|---|---|
| **8** | Automated security layers |
| **12** | Intentional, documented vulnerabilities (CWE + OWASP mapped) |
| **7** | Gated CI/CD jobs (GitHub Actions) |
| **1** | Command to bring the full runtime stack up |

---

## Architecture

<p align="center">
  <img width="667" height="360" alt="image" src="https://github.com/user-attachments/assets/a57003aa-b35a-4442-8fb1-06370970868c" />
</p>

---

## The Vulnerable Application

A full Flask app — login, registration, blog, todo manager, admin panel,
REST API with JWT — built with intentional, working vulnerabilities so the
pipeline has something real to catch:

| # | Vulnerability | CWE |
|---|---|---|
| 1 | SQL Injection (auth bypass) | CWE-89 |
| 2 | Stored XSS | CWE-79 |
| 3 | Weak password hashing (MD5, no salt) | CWE-327/916 |
| 4 | Hardcoded secret key | CWE-798 |
| 5 | No CSRF protection | CWE-352 |
| 6 | IDOR / broken object-level authorization | CWE-639 |
| 7 | Broken access control | CWE-284 |
| 8 | Sensitive data exposure | CWE-200 |
| 9 | Unrestricted file upload | CWE-434 |
| 10 | JWT algorithm confusion | CWE-347 |
| 11 | Verbose error / stack trace leakage | CWE-209/215 |
| 12 | Missing security headers | CWE-16 |

Full detail and reproduction steps: [`docs/MODULE-0-VULNERABLE-APP.md`](docs/MODULE-0-VULNERABLE-APP.md)

<p align="center">
  <img width="932" height="435" alt="image" src="https://github.com/user-attachments/assets/ba0347e9-0cf6-4186-881d-aa373cdbf1ba" />
</p>

---

## Security Layers

| Layer | What it does | Docs |
|---|---|---|
| **1. Pre-Commit** | Bandit, Semgrep, detect-secrets block bad commits locally | [MODULE-1](docs/MODULE-1-PRE-COMMIT.md) |
| **2. Dependencies** | pip-audit, Safety, CycloneDX SBOM — fails on HIGH/CRITICAL CVEs | [MODULE-2](docs/MODULE-2-DEPENDENCY-SECURITY.md) |
| **3. CI/CD** | GitHub Actions — 7 gated jobs, stops on any failure | [MODULE-3](docs/MODULE-3-CICD-SECURITY.md) |
| **4. Container** | Multi-stage, non-root, read-only, Trivy + Hadolint | [MODULE-4](docs/MODULE-4-CONTAINER-SECURITY.md) |
| **5. Infrastructure** | Terraform on AWS Free Tier, Checkov + tfsec gated | [MODULE-5](docs/MODULE-5-INFRASTRUCTURE.md) |
| **6. DAST** | OWASP ZAP authenticated spider + active scan | [MODULE-6](docs/MODULE-6-DAST.md) |
| **7. Network** | Nmap + Shodan exposure checks, webhook alerts | [MODULE-7](docs/MODULE-7-NETWORK-SECURITY.md) |
| **8. Monitoring + AI** | Prometheus, Grafana, Ollama-generated incident reports | [MODULE-8](docs/MODULE-8-MONITORING-AI.md) |

---

## Screenshots
<img width="900" height="432" alt="image" src="https://github.com/user-attachments/assets/90eb9532-fb33-4dea-8ab5-773a0247a328" />
<img width="1835" height="1016" alt="image" src="https://github.com/user-attachments/assets/81339c43-438e-4105-9407-44a61d3d9eea" />
<img width="667" height="360" alt="image" src="https://github.com/user-attachments/assets/beb0d1a1-178f-42ef-aad8-0fb235c8eee3" />
<img width="932" height="435" alt="image" src="https://github.com/user-attachments/assets/6984f8b1-2656-4680-a537-ae52525f2bdf" />
<img width="1688" height="892" alt="image" src="https://github.com/user-attachments/assets/4bd0fadb-7cc3-4d82-96e7-3d7c89f0a661" />
<img width="1680" height="1019" alt="image" src="https://github.com/user-attachments/assets/efc93efe-3a1e-45ad-a2ad-de6ac24d49a3" />



### 1. Bandit Output
<p align="center">
  <img width="1447" height="431" alt="image" src="https://github.com/user-attachments/assets/1646a05f-9692-4b6f-822b-0e91d454ba84" />
</p>

### 2. Dependency Scan / SBOM Output
<p align="center">
  <img width="1420" height="588" alt="image" src="https://github.com/user-attachments/assets/768e837c-5b64-444f-8417-dfff9b559f59" />
</p>

### 3. Dependency CVEs — pip-audit
<p align="center">
  <img width="1412" height="936" alt="image" src="https://github.com/user-attachments/assets/728ae131-47d6-4b8a-b2b8-893bd1dacceb" />

</p>

### 4. Running Containers
<p align="center">
  <img width="1201" height="307" alt="image" src="https://github.com/user-attachments/assets/a160b122-2936-4e88-abd8-cb8efec1d561" />
</p>

### 5. Terraform Apply Output
<p align="center">
  <img width="1415" height="890" alt="image" src="https://github.com/user-attachments/assets/7cb63308-4f11-41ac-9789-e701ddfbb26a" />
</p>

### 6. OWASP ZAP DAST Report
<p align="center">
  <img width="1680" height="1019" alt="image" src="https://github.com/user-attachments/assets/612d9ca2-0550-46fa-837d-2eb3ff76a62a" />
</p>

### 7. Software Bill of Materials 
<p align="center">
  <img width="1415" height="379" alt="image" src="https://github.com/user-attachments/assets/cea1c761-d697-4cf5-a996-e0b9e04a7f92" />
</p>

### 8. Grafana Dashboard
<p align="center">
  <img width="1672" height="1011" alt="image" src="https://github.com/user-attachments/assets/7139e2c5-cba3-401a-be31-357e5e111d98" />
</p>

### 9. AI-Generated Incident Report
<p align="center">
  <img width="1688" height="892" alt="image" src="https://github.com/user-attachments/assets/a2bc7da6-a279-40f3-ab09-6549eded612e" />
</p>

---

## Getting Started

Full step-by-step setup (Windows/macOS/Linux) is in
[`docs/SETUP-AND-RUN-GUIDE.md`](docs/SETUP-AND-RUN-GUIDE.md). Quick version:

```bash
git clone <your-repo-url>
cd secureapp-pipeline

# Python tooling
python3 -m venv venv && source venv/bin/activate
pip install -r src/requirements.txt -r requirements-dev.txt -r ai/requirements.txt

# Full runtime stack (app + Prometheus + Grafana + Ollama + AI service)
cd docker
docker compose up -d --build
docker compose exec ollama ollama pull llama3.1
```

Then open:
- App — http://localhost:5000
- Grafana — http://localhost:3000
- AI service docs — http://localhost:8000/docs
- Prometheus — http://localhost:9090

---

## Project Structure

```
secureapp-pipeline/
├── src/                  # Flask application (Level 0)
├── ai/                   # FastAPI + Ollama log analysis service (Level 8)
├── docker/               # Dockerfile, docker-compose.yml (Levels 4 + 8)
├── terraform/             # AWS infrastructure as code (Level 5)
├── dast/                 # OWASP ZAP automation config (Level 6)
├── monitoring/            # Prometheus + Grafana configs (Level 8)
├── scripts/               # Orchestration scripts for every level
├── tests/                 # pytest suite
├── docs/                  # Per-module setup guides + this README's screenshots
├── .github/workflows/     # CI/CD pipeline (Level 3)
├── .pre-commit-config.yaml
├── .checkov.yaml / .tfsec.yml
└── .hadolint.yaml
```

---

## Documentation

| Guide | Covers |
|---|---|
| [SETUP-AND-RUN-GUIDE.md](docs/SETUP-AND-RUN-GUIDE.md) | Full PC setup, running everything together |
| [MODULE-0](docs/MODULE-0-VULNERABLE-APP.md) → [MODULE-8](docs/MODULE-8-MONITORING-AI.md) | Deep dive per security layer |

---

## Tech Stack

Python · Flask · SQLite · Docker · Docker Compose · Terraform ·
GitHub Actions · Bandit · Semgrep · detect-secrets · pip-audit · Safety ·
CycloneDX · Trivy · Hadolint · Docker Bench · Checkov · tfsec ·
OWASP ZAP · Nmap · Shodan · Prometheus · Grafana · FastAPI · Ollama

---

## Future Scope

- Kubernetes orchestration with OPA/Gatekeeper policies
- WAF + rate limiting in front of the application
- SOAR-style automated response to AI-flagged incidents
- Multi-cloud Terraform modules (Azure / GCP)
- Mobile app + expanded Zero Trust access model

---

## License

MIT — see [LICENSE](LICENSE) for details.

