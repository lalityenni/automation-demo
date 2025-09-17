# automation-demo

An automation workflow using **Azure Functions** as the orchestration glue between enterprise systems and **Terraform** provisioning (via GitHub Actions).

## Structure

automation-demo/
├─ functions/          # Azure Functions code
│  ├─ IngestRequest/   # HTTP trigger (receives requests)
│  ├─ ProvisionJob/    # Queue trigger (provisions infra)
│  ├─ host.json        # Global Functions settings
│  └─ requirements.txt # Python dependencies
├─ terraform/          # Terraform IaC skeleton
│  ├─ main.tf
│  └─ variables.tf
├─ .gitignore
└─ README.md

## Notes
- We only **write code locally**; deployment happens later via CI/CD.
- `functions/` holds the Azure Function stubs (`__init__.py` + `function.json`).
- `terraform/` will grow into real infra code in later modules.