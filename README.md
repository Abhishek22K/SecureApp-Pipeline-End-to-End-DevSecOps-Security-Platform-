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

<img width="667" height="360" alt="image" src="https://github.com/user-attachments/assets/a57003aa-b35a-4442-8fb1-06370970868c" />

<p align="center">
  <img src="docs/screenshots/02-architecture.png" alt="8-layer architecture diagram" width="800">
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

<img width="932" height="435" alt="image" src="https://github.com/user-attachments/assets/ba0347e9-0cf6-4186-881d-aa373cdbf1ba" />

<p align="center">
  <img src="docs/screenshots/03-app-running.png" alt="Vulnerable app running in browser" width="700">
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


### 1. Pre-Commit Hooks Blocking a Vulnerable Commit
*What to capture: your terminal after running `git commit`, showing
Bandit/Semgrep/detect-secrets output and the commit being rejected.*
<p align="center">
  <img src="docs/screenshots/04-precommit-blocked.png" alt="Pre-commit hooks blocking a commit" width="750">
</p>

### 2. Dependency Scan / SBOM Output
*What to capture: terminal output of `bash scripts/run-level2-checks.sh`,
or the generated `reports/sbom.cyclonedx.json` opened in your editor.*
<p align="center">
  <img src="docs/screenshots/05-dependency-scan.png" alt="pip-audit and SBOM generation output" width="750">
</p>

### 3. GitHub Actions Pipeline Run
*What to capture: the Actions tab on GitHub showing all 7 jobs
(test → sast/secrets-scan/dependency-scan → build-image → dast → push-image → deploy).*
<p align="center">
  <img src="docs/screenshots/06-cicd-pipeline.png" alt="GitHub Actions pipeline run" width="750">
</p>

### 4. Running Containers
*What to capture: `docker compose ps` output, or Docker Desktop's
Containers tab showing all 5 services healthy.*
<p align="center">
  <img src="docs/screenshots/07-docker-containers.png" alt="Docker containers running" width="750">
</p>

### 5. Terraform Apply Output
*What to capture: terminal output of `terraform apply`, or the AWS Console
showing the created VPC/EC2/S3 resources.*
<p align="center">
  <img src="docs/screenshots/08-terraform-apply.png" alt="Terraform apply output" width="750">
</p>

### 6. OWASP ZAP DAST Report
*What to capture: `reports/zap-report.html` opened in a browser, showing
the risk-ranked alert list.*
<p align="center">
  <img src="docs/screenshots/09-zap-report.png" alt="OWASP ZAP DAST report" width="750">
</p>

### 7. Nmap / Network Scan Results
*What to capture: terminal output of `bash scripts/run-level7-checks.sh`
showing the open-port table.*
<p align="center">
  <img src="docs/screenshots/10-nmap-scan.png" alt="Nmap network scan results" width="750">
</p>

### 8. Grafana Dashboard
*What to capture: http://localhost:3000 — the "SecureApp Pipeline"
dashboard with live metrics (ideally after generating some login-failure
traffic so the panels aren't empty).*
<p align="center">
  <img src="docs/screenshots/11-grafana-dashboard.png" alt="Grafana monitoring dashboard" width="750">
</p>

### 9. AI-Generated Incident Report
*What to capture: the JSON response from `POST /incident-report`
(http://localhost:8000/docs is the easiest place to trigger and view it).*
<p align="center">
  <img src="docs/screenshots/12-ai-incident-report.png" alt="AI-generated incident report" width="750">
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

