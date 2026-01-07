# Changelog

All notable changes to this project will be documented here.

The format is based on Keep a Changelog
and this project follows Semantic Versioning.

---

## [0.3.0] – 2026-01-08

### Added
- Interactive CLI menu with:
  - Built-in presets
  - User presets
  - Preset creation
  - File finder across presets
- Custom preset system
  - Create once, reuse anywhere
  - Stored in `~/.initforge/presets`
- Config mode via `.initforge.yaml`
- `--dry-run` mode to preview changes
- `--save-config` flag to persist setup
- File finder tool to locate templates (logger, config, etc.)
- Better README auto-generation with:
  - Env setup
  - Install steps
  - Run command

### Improved
- UX flow for beginners (bootcamp friendly)
- Preset handling: built-in + custom unified
- Validation for Python versions
- Safer overwrite logic for README and files

### Fixed
- Template loading issues in packaged installs
- Missing package-data for templates
- CLI crashes from invalid preset imports
- Config and preset conflict handling

---

## [0.2.0]

- Added preset system (base, ML, Streamlit)
- YAML config support
- Python version validation
- Better generator structure

---

## [0.1.0]

- Initial release
- Basic project scaffolding
- Auto README generation
- GitHub → Local → Env → Run workflow
