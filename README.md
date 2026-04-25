# Steve's Installed Software Tools
*Generated: 2026-04-04*

---

## Core CLI Tools (in PATH)

| Tool | Version/Notes |
|------|--------------|
| gcc/g++ | 13.3.0 (also 12.x) |
| clang | 18.1.3 |
| gdb | installed |
| make | installed |
| cmake | 3.28.3 |
| git | installed |
| python3/pip3 | system Python |
| perl | installed |
| gawk, sed, awk | installed |
| curl, wget | installed |
| nvcc | CUDA (NVIDIA) |
| octave | installed |
| julia | via juliaup (v1.12) |
| node/npm | v20.19.6 active; v18.20.0, v22.21.1 also installed (nvm) |
| ollama | /usr/local/bin |
| ffmpeg | 6.1.1 |
| sox | installed |
| blender | 4.0.2 |
| openscad | installed |
| kicad | installed |
| ngspice | installed |
| iverilog | installed |
| verilator | installed |
| yosys | installed |
| z3 | installed |
| java/javac | OpenJDK 21 |
| sdcc | Small Device C Compiler (Z80, 8051, STM8, PIC, AVR) |
| avrdude | 7.1 |
| avr-gcc/binutils | binutils-avr (AVR cross toolchain) |
| arduino | 1.8.19 (apt) |
| arduino-cli | 1.3.0 (snap) |
| cppcheck | 2.13.0 |
| build-essential | 12.10 |
| autoconf/automake | installed |
| fldigi | 4.2.03 (amateur radio digital modes) |
| bladerf | 0.2023.02 (SDR) |
| bpftrace | 0.20.2 |
| bpfcc-tools | 0.29.1 |
| clamav | 1.4.3 |
| duplicity | 2.1.4 |
| firebird3.0 | 3.0.11 (embedded DB) |
| cycfx2prog | 0.47 (Cypress FX2 programmer) |
| sigrok-cli | 0.7.2 (logic analyzer CLI) |
| pulseview | 0.4.2 (logic analyzer GUI, sigrok frontend) |
| gamemode | 1.8.1 |
| castxml | 0.6.3 |
| freeglut3 | 3.4.0 |

---

## ~/opt (locally built, not in apt)

| Tool | Version | Notes |
|------|---------|-------|
| openEMS | 0.0.36 | FDTD electromagnetic solver — antennas, waveguides, photonics (MZI, ring resonators), RF |
| CSXCAD | 0.6.3 | Geometry/material engine for openEMS |
| VTK | 9.3.1 | Built from source into ~/opt/vtk (minimal: IOGeometry, IOPLY, CommonCore) — avoids conflict with system ParaView |
| micromamba | latest | Lightweight conda in ~/opt/bin/micromamba |
| Qucs-S | s25.2.0 | RF/circuit sim with ngspice backend, S-params, AC/DC/transient. `~/opt/qucs-s/`. Launch: `qucs-s` |

**openEMS paths** (in `~/.bashrc`):
- Binaries: `~/opt/openEMS/bin`
- Libs: `~/opt/openEMS/lib`, `~/opt/vtk/lib` (via `LD_LIBRARY_PATH`)
- Python: `pip install`ed — `from CSXCAD import ContinuousStructure; from openEMS import openEMS`
- MCP tool: `openems_sim` in engineering MCP server

**sigrok MCP tool** (`sigrok_run` in engineering MCP server):
- Modes: `list`, `scan`, `list_serial`, `decode_file`, `capture`, `demo`, `show_decoder`, `raw`
- 100+ protocol decoders: spi, uart, i2c, i2s, can, usb, 1-wire, jtag, pwm, avr_isp, ...
- Hardware: fx2lafw (Cypress FX2 logic analyzers), `/dev/ttyUSB0` detected
- PulseView (GUI) launched manually for visual waveform inspection

---

## /usr/local/bin

| Tool | Notes |
|------|-------|
| ollama | Local LLM runner |
| claude | Claude Code CLI |
| gemini | Gemini CLI |
| grok | Grok CLI |
| WolframKernel | Wolfram Engine kernel |
| cap32 | Amstrad CPC464 emulator |

---

## ~/.local/bin

| Tool | Notes |
|------|-------|
| uv | Fast Python package manager |
| uvx | uv tool runner |
| llm | Simon Willison's LLM CLI |
| marimo | Reactive Python notebook |
| openai | OpenAI CLI |
| huggingface-cli / hf | HuggingFace Hub CLI |
| tiny-agents | MCP-based agent runner |
| mcp | MCP server CLI |
| transformers-cli | HuggingFace transformers CLI |
| accelerate | HuggingFace accelerate CLI |
| browsh | Terminal web browser |
| carbonyl | Chromium-based terminal browser |
| w3m | Text web browser |
| direnv | Per-directory env vars |
| deepseek | DeepSeek CLI |
| gemini-ai | Gemini AI CLI |
| sqlite-utils | SQLite CLI toolkit |
| Telegram | Telegram desktop |
| tuir / rtv | Reddit terminal clients |
| typer | CLI builder CLI |
| tqdm | Progress bar CLI |
| torchrun | PyTorch distributed launcher |
| uvicorn | ASGI server |
| websockets | WebSocket CLI |

---

## Snap Packages

| Package | Version |
|---------|---------|
| chromium | 146.0.7680.164 |
| firefox | 149.0 |
| thunderbird | 140.9.0esr |
| vlc | 3.0.20 |
| code (VSCode) | e7fb5e96 |
| arduino-cli | 1.3.0 |
| adguard-home | v0.107.73 |
| glow | 2.1.1 (Markdown renderer) |
| mdless | 1.0.33 |
| luanti | 5.14.0 (Minetest) |
| the-powder-toy | v99.3.384 |
| gemini | 4.4.1 |
| snap-store | 41.3 |
| firmware-updater | 0+git.7d22721 |

---

## Python Packages (pip3)

### AI / ML
| Package | Version |
|---------|---------|
| torch | 2.2.2+cpu |
| torchvision | 0.25.0+cpu |
| torchaudio | 2.10.0+cpu |
| transformers | 4.57.6 |
| accelerate | 1.12.0 |
| huggingface-hub | 0.36.2 |
| safetensors | 0.7.0 |
| sentencepiece | 0.2.0 |
| tokenizers | 0.22.2 |
| opencv-python | 4.8.1.78 |
| gguf | 0.10.0 |

### LLM / API Clients
| Package | Version |
|---------|---------|
| anthropic | 0.88.0 |
| openai | 2.24.0 |
| google-generativeai | 0.8.6 |
| google-api-python-client | 2.187.0 |
| llm | 0.28 |
| mcp | 1.27.0 |
| wolframalpha | 5.1.3 |
| ollama | (via CLI) |

### ROS2 (Jazzy/Humble)
- rclpy, ros2cli, ros2topic, ros2node, ros2param, ros2service, ros2action
- ros2launch, ros2bag, ros2component, ros2doctor, ros2interface
- tf2-ros-py, tf2-geometry-msgs, tf2-sensor-msgs, tf2-kdl, tf2-tools
- launch, launch-ros, launch-testing, launch-testing-ros
- Full message types: geometry_msgs, sensor_msgs, nav_msgs, std_msgs, visualization_msgs, etc.
- ament build tools: ament-cmake, ament-lint, ament-copyright, etc.

### Scientific / Numerical
| Package | Version |
|---------|---------|
| numpy | 1.26.4 |
| scipy | 1.11.4 |
| matplotlib | 3.6.3 |
| sympy | 1.14.0 |
| mpmath | 1.3.0 |
| mpi4py | 3.1.5 |
| networkx | 3.6.1 |

### Web / Networking
| Package | Version |
|---------|---------|
| httpx | 0.28.1 |
| requests | 2.31.0 |
| uvicorn | 0.42.0 |
| starlette | 1.0.0 |
| websockets | 16.0 |
| beautifulsoup4 | 4.12.3 |
| playwright | (npm) |
| paramiko | 2.12.0 |

### GUI / Visualization
| Package | Version |
|---------|---------|
| wxPython | 4.2.1 |
| PyQt5 | 5.15.10 |
| PyQt6 | 6.6.1 |
| PyQt-Qwt | 1.2.2 |
| pyqtgraph | 0.13.4 |
| PyOpenGL | 3.1.7 |
| Pillow | 10.2.0 |

### Hardware / Serial
| Package | Version |
|---------|---------|
| pyserial | 3.5 |
| sounddevice | 0.5.5 |
| SpeechRecognition | 3.14.5 |
| bcc | 0.29.1 |

### Data / Dev Tools
| Package | Version |
|---------|---------|
| sqlite-utils | 3.39 |
| marimo | 0.22.0 |
| pydantic | 2.12.5 |
| pytest | 7.4.4 |
| flake8 | 7.0.0 |
| tabulate | 0.9.0 |
| rich | 13.7.1 |
| Jinja2 | 3.1.2 |
| PyYAML | 6.0.1 |
| python-dotenv | 1.2.2 |
| python-docx | 1.2.0 |
| xmltodict | 1.0.4 |

### Electromagnetics / EDA
| Package | Version | Notes |
|---------|---------|-------|
| CSXCAD | 0.6.3 | Geometry/structure definition for openEMS |
| openEMS | 0.0.36 | Python bindings for FDTD solver |
| h5py | 3.16.0 | HDF5 file I/O (openEMS simulation output) |
| cython | 3.2.4 | Required to build openEMS Python extensions |
| pymeep | 1.33-beta | MIT MEEP FDTD photonics sim (conda env, numpy 1.26.4). MCP: `meep_sim` |
| scikit-rf | 1.11.0 | RF/microwave S-params, touchstone, network analysis. MCP: `skrf_eval` |
| gdstk | 1.0.0 | GDSII/OASIS layout generation (photonics, silicon fab). MCP: `gdstk_script` |
| pyvisa | 1.16.2 | VISA instrument control (USB-TMC/LAN/GPIB/serial). MCP: `pyvisa_instrument` |
| pyvisa-py | 0.8.1 | Pure-Python VISA backend (no NI-VISA driver needed) |
| zeroconf | 0.148.0 | LAN instrument discovery (VXI-11/HiSlip via mDNS) |
| pymeasure | 0.15.0 | Lab instrument abstraction (Keithley, Rigol, Siglent, etc) |
| PySpice | 1.5 | Python → ngspice interface (import as `PySpice`) |
| lcapy | 1.26 | Symbolic linear circuit analysis using sympy |
| schemdraw | 0.22 | Circuit diagram drawing in Python |
| skidl | 2.2.2 | Netlist description in Python, KiCad export |

### Security / Crypto
| Package | Version |
|---------|---------|
| cryptography | 41.0.7 |
| PyJWT | 2.12.1 |
| bcrypt | 3.2.2 |
| PyNaCl | 1.5.0 |
| praw | 7.8.1 (Reddit API) |

---

## Node.js Global Packages (npm -g)

| Package | Version |
|---------|---------|
| @anthropic-ai/claude-code | 2.1.92 |
| @google/gemini-cli | 0.36.0 |
| @google/generative-ai | 0.24.1 |
| @modelcontextprotocol/server-filesystem | 2026.1.14 |
| playwright | 1.58.2 |
| netlistsvg | 1.0.2 |
| single-file-cli | 2.0.83 |
| corepack | 0.34.1 |
| npm | 10.8.2 |

---

## Summary

| Category | Count |
|----------|-------|
| apt/dpkg packages | 3,653 |
| Python packages | ~250 |
| Node.js versions | 3 (v18, v20, v22) |
| npm global packages | 9 |
| Snap packages | 31 |

---

## TODO — Engineering Gaps to Fill

Priority order for hardware/EE/RF work.

### RF / EM Simulation
| Tool | Install | Why |
|------|---------|-----|
| ~~OpenEMS~~ ✅ | built from source `~/opt/openEMS` | FDTD EM solver — done |
| ~~xnec2c~~ ✅ | 4.4.12, apt | NEC2 antenna modelling, native Linux |
| ~~Qucs-S~~ ✅ | s25.2.0 AppImage at `~/opt/qucs-s/`, launcher at `~/.local/bin/qucs-s` | Circuit sim with ngspice backend, S-param focus, better UI than raw ngspice. GUI only, launch with `qucs-s` |

### FPGA / HDL
| Tool | Install | Why |
|------|---------|-----|
| ~~GHDL~~ ✅ | 4.1.0, apt | VHDL simulator. Tested: 4-bit counter, field decayed at 100ns. MCP: `ghdl_sim` |
| ~~nextpnr~~ ✅ | 0.6, apt (ice40 + ecp5) | Place-and-route. Tested: blinky → iCE40 hx8k, 27 LCs, 194 MHz max. MCP: `nextpnr_pnr` |
| ~~Project IceStorm~~ ✅ | apt (icepack, iceprog, icetime) | iCE40 bitstream tools. icepack + icetime included in nextpnr_pnr |
| ~~cocotb~~ ✅ | 2.0.1, pip | Python HDL testbench. Tested: AND gate, TESTS=1 PASS=1. MCP: `cocotb_test` |
| ~~SymbiYosys~~ ✅ | built from source (`/usr/local/bin/sby`), z3 backend | Formal verification. Tested: mux proven correct by k-induction. MCP: `symbiyosys_check` |

### Python EE Packages
| Package | Install | Why |
|---------|---------|-----|
| ~~scikit-rf~~ ✅ | 1.11.0, pip installed | S-params, touchstone, transmission line analysis, network cascading. MCP tool: `skrf_eval` |
| ~~gdstk~~ ✅ | 1.0.0, pip installed | GDSII layout for memR photonic design (waveguides, MZI, ring resonators). MCP tool: `gdstk_script` |
| ~~pyspice~~ ✅ | 1.5, pip (import as `PySpice`) | Python → ngspice interface |
| ~~lcapy~~ ✅ | 1.26, pip | Symbolic linear circuit analysis (sympy-based) |
| ~~schemdraw~~ ✅ | 0.22, pip | Draw circuit diagrams programmatically |
| ~~skidl~~ ✅ | 2.2.2, pip | Describe netlists in Python, export to KiCad |
| ~~pyvisa~~ ✅ | 1.16.2 + pyvisa-py 0.8.1 + zeroconf, pip | USB-TMC/LAN/GPIB/serial SCPI instrument control, no NI-VISA needed. MCP: `pyvisa_instrument` |
| ~~pymeasure~~ ✅ | 0.15.0, pip | Lab instrument abstraction (Keithley, Rigol, Siglent, etc) |

### Photonics (memR-relevant)
| Tool | Install | Why |
|------|---------|-----|
| ~~KLayout~~ ✅ | 0.28.16, apt installed | GDSII/OASIS viewer + headless scripting via pya API. MCP tool: `klayout_script` (DRC, inspection, layout manipulation) |
| ~~MEEP~~ ✅ | pymeep 1.33-beta, conda env `~/opt/bin/micromamba run -n meep` (numpy pinned <2 for Core2 CPU) | MIT FDTD photonics sim — waveguides, MZI, ring resonators, photonic crystals. Tested: 2D Si waveguide 16s. MCP tool: `meep_sim` |
| ~~MPB~~ ✅ | 1.11.1, apt | Photonic band structure calculator (MIT), uses libctl 4.5.1 |

### FEM / Multiphysics
| Tool | Install | Why |
|------|---------|-----|
| ~~Elmer FEM~~ ✅ | v26.1, PPA `elmer-csc-ubuntu/elmer-csc-ppa`, binaries: ElmerSolver, ElmerGrid | Open multiphysics — EM, thermal, structural, fluid |
| Salome | [download](https://www.salome-platform.org) | FEM pre/post-processor, works with Elmer — not yet installed |

### Logic Analyzer / Instruments
| Tool | Install | Why |
|------|---------|-----|
| ~~sigrok + PulseView~~ ✅ | already installed (sigrok-cli 0.7.2, pulseview 0.4.2, fx2lafw firmware) | Used in `~/tec-scope/` to verify SPI signals (CS/SCK/MOSI) on Z80 telescope controller. MCP tool `sigrok_run` added — 7 modes: list, scan, list_serial, decode_file, capture, demo, show_decoder, raw. PulseView is GUI-only (launch manually). `/dev/ttyUSB0` detected. |
| ~~openhantek~~ ✅ | 3.4.0, tarball at `~/opt/openhantek/`, launcher `~/.local/bin/openhantek` | DSO software for Hantek USB scopes |

---

## Tool Chain Combinations & Applications

### Electronics / Circuit Design

| Chain | Application |
|-------|-------------|
| `lcapy` → `schemdraw` → `matplotlib` | Symbolic circuit analysis + rendered diagram |
| `lcapy` → `sympy` → `matplotlib` | Analytical transfer functions, Laplace/z-domain |
| `schemdraw` → `skidl` → KiCad netlist | Draw schematic → generate netlist programmatically |
| `skidl` → `netlistsvg` | Python netlist → SVG schematic render |
| `PySpice` → `ngspice` → `matplotlib` | Python-described circuit → SPICE sim → plot |
| `lcapy` → `PySpice` → `ngspice` | Symbolic design → SPICE verification |
| KiCad (EasyEDA export) → `ngspice` | Full PCB flow → netlist sim |
| `schemdraw` → PDF/PNG | Publication-quality circuit diagrams |

---

### RF / EM Simulation

| Chain | Application |
|-------|-------------|
| `scikit-rf` → `matplotlib` | S-param network analysis, Smith charts |
| `scikit-rf` → touchstone `.s2p` → Qucs-S | Python-generated networks → RF circuit sim |
| `openEMS` → `h5py` → `matplotlib` | FDTD field data → custom plots |
| `openEMS` → VTK → ParaView | 3D field visualization |
| Qucs-S (`ngspice` backend) → S-params | RF/AC sim with GUI |
| `openEMS` + `scikit-rf` | FDTD geometry → extract S-params → network cascade |
| `xnec2c` → antenna patterns | NEC2 antenna modeling |
| `GNURadio` + `bladerf` → `sigrok` | SDR capture → protocol decode |
| `MEEP` → `scikit-rf` | Photonic FDTD → extract RF-style S-params |

---

### Photonics / memR-specific

| Chain | Application |
|-------|-------------|
| `gdstk` → KLayout DRC | Python layout generation → design rule check |
| `gdstk` → KLayout → GDS export | Full photonic chip tape-out prep |
| `MEEP` → `matplotlib` | MZI/waveguide FDTD → field plots |
| `MEEP` → `h5py` → `matplotlib` | Time-domain fields → frequency analysis |
| `MPB` → band structure → `matplotlib` | Photonic crystal band gaps |
| `openEMS` → `MEEP` (cross-validate) | FDTD solver comparison for MZI design |
| `gdstk` → `MEEP` (import geometry) | Layout → simulation geometry |
| `scikit-rf` + `MEEP` | MZI as RF network → cascade multiple stages |
| `lcapy` → MZI transfer matrix | Symbolic phase-coded neuron math |

---

### FPGA / HDL

| Chain | Application |
|-------|-------------|
| Verilog → `iverilog` → VCD → `sigrok` | Simulate → decode waveforms with protocol analyzers |
| Verilog → `verilator` lint → `yosys` → `nextpnr` → `icepack` → `iceprog` | Full iCE40 FPGA synthesis + flash |
| Verilog → `cocotb` (Python testbench) → `iverilog`/`verilator` | Python-driven HDL testing |
| Verilog → `SymbiYosys` + `z3` | Formal verification (k-induction, BMC) |
| VHDL → `GHDL` → VCD → `sigrok` | VHDL sim → waveform analysis |
| VHDL → `cocotb` → `GHDL` | Python testbench for VHDL |
| `yosys` → `nextpnr` → timing report | Synthesis + place-and-route analysis |
| `SymbiYosys` → `z3` → proof | SMT-based equivalence checking |
| Verilog → `yosys` → netlist → `netlistsvg` | Logic netlist visualization |

---

### Embedded / Microcontrollers

| Chain | Application |
|-------|-------------|
| C → `avr-gcc` → `avrdude` | AVR firmware compile + flash |
| C → `avr-gcc` → `gdb` | AVR on-chip debug |
| Z80 ASM → `sdcc` → RC2014/TEC-1 | Z80 assembly → flash to hardware |
| `sdcc` (C) → Z80 hex → `cap32` | C → Amstrad CPC464 emulation test |
| `arduino-cli` → AVR/ESP32 | Arduino framework compile + upload |
| `sigrok` + `fx2lafw` → SPI/I2C/UART decode | Logic analyzer capture on `/dev/ttyUSB0` |
| `pyserial` → `sigrok` (compare) | Software serial vs hardware capture cross-check |
| `pyvisa` + `pymeasure` → instrument control | Automated bench measurement |
| `pyvisa` → Rigol/Siglent SCPI → `matplotlib` | Capture scope data → plot in Python |

---

### AI / ML

| Chain | Application |
|-------|-------------|
| `torch` → train → `safetensors` → `transformers` | Full training → HuggingFace-compatible model |
| `torch` → `accelerate` → multi-GPU | Distributed training |
| `huggingface-cli` → download → `transformers` | Pull + run pretrained models |
| `ollama` → local LLM inference | On-device inference (no API) |
| `anthropic` SDK → Claude API | Production Claude integration |
| `torch` (TinyML) → quantize → ESP32 (`arduino-cli`) | Edge ML deployment |
| `Octave` prototype → `numpy`/`scipy` port | Algorithm exploration → Python production |
| `Julia` → `numpy` (compare) | High-performance numerics cross-validation |
| `ollama` → `mcp` server → Claude Code | Local LLM as MCP tool backend |
| Wolfram Engine (`WolframKernel`) → `sympy` (compare) | CAS cross-validation |

---

### Signal Processing / Audio / SDR

| Chain | Application |
|-------|-------------|
| `sox` → `ffmpeg` | Audio format conversion + processing pipeline |
| `sox` → `matplotlib` (via numpy) | Audio waveform/spectrum analysis |
| `GNURadio` → `bladerf` → `sigrok` | SDR receive → protocol decode |
| `GNURadio` → `fldigi` | SDR → digital amateur radio modes |
| `ffmpeg` → `whisper.cpp` | Video/audio → local speech-to-text |
| `sigrok` → `pulseview` | CLI capture → GUI waveform review |
| `sigrok` decode → `matplotlib` | Protocol timing → Python plot |

---

### Scientific / Mathematical

| Chain | Application |
|-------|-------------|
| `sympy` → `numpy`/`scipy` → `matplotlib` | Symbolic derivation → numerical eval → plot |
| `Wolfram` → `sympy` (cross-check) | CAS agreement verification |
| `z3` → SMT solution → `sympy` | Constraint solving → symbolic verification |
| `scipy` → `matplotlib` | Numerical simulation → publication plots |
| `Julia` → `numpy` (via file I/O) | High-perf compute → Python postprocess |
| `mpmath` → arbitrary precision | Where float64 isn't enough |
| `networkx` → graph analysis → `matplotlib` | Neural/circuit topology analysis |
| `mpi4py` → distributed `scipy` | HPC-style parallel numerics |

---

### CAD / Physical Fabrication

| Chain | Application |
|-------|-------------|
| `FreeCAD` → STL → MakeraCAM | 3D model → CNC toolpaths |
| `OpenSCAD` → STL → 3D print | Parametric model → print |
| `Blender` → STL → `FreeCAD` | Mesh → CAD refinement |
| `gdstk` → GDS → KLayout → fab | Silicon photonic layout → foundry |
| `FreeCAD` + `openEMS` | Mechanical geometry → EM simulation |
| EasyEDA → KiCad → `skidl` | Schematic → programmable netlist |

---

### Cross-Domain Power Chains

| Chain | Application |
|-------|-------------|
| `lcapy` → `PySpice` → `ngspice` → `scikit-rf` → `openEMS` | Full signal chain: symbolic → SPICE → RF → FDTD |
| `gdstk` → KLayout DRC → `MEEP` → `scikit-rf` | Photonic layout → simulate → extract network params |
| `GHDL`/`iverilog` → `cocotb` → `SymbiYosys`+`z3` → `yosys` → `nextpnr` → FPGA | Full HDL design + verify + implement |
| `torch` (train) → `ollama` (serve) → `mcp` → Claude Code | Local ML model → MCP tool |
| `pyvisa`/`pymeasure` → `scipy` → `matplotlib` | Instrument → data → analysis |
| `sigrok` + `fx2lafw` → decode → `matplotlib` | Hardware capture → software analysis |
| Z80 ASM → `sdcc` → `cap32` (emulate) → RC2014 (hardware) | Write → test virtually → deploy physically |
| `Octave` → `numpy` → `torch` | Algorithm prototype → ML integration |
| `openEMS` + `MEEP` (dual validate) → `gdstk` → KLayout | Dual-FDTD validated photonic design → layout |

---

## Project → Tool Chain Mapping

| Project | Domain | Primary Tool Chains |
|---------|--------|---------------------|
| `~/memR/` | Phase-coded neuromorphic computing | `lcapy` → MZI transfer matrix; `Octave`/`scipy`/`numpy` → phase simulation; `MEEP` → MZI FDTD; `openEMS` + `MEEP` cross-validate; `gdstk` → KLayout DRC → fab; `scikit-rf` → cascade stages; `sdcc`/Z80 ASM → RC2014 universal interface; `sympy` → analytical neuron math |
| `~/vl-jepa/` | Vision-Language self-supervised learning | `torch` → train → `safetensors` → `transformers`; `accelerate` multi-GPU; `huggingface-cli` → pretrained models; `ollama` → local inference test |
| `~/soma/` | Embodied cognition / robot nervous system | ROS2 (`rclpy`, `ros2topic`, `tf2`) → motor control; `torch` → inference; `pyserial` → hardware drivers; `pyvisa`/`pymeasure` → sensors; `numpy`/`scipy` → predictive models |
| `~/tinyml/` | Edge ML on ESP32/microcontrollers | `torch` → quantize → TFLite → `arduino-cli` flash; `avr-gcc` → `avrdude`; `sigrok` → verify comms; `numpy`/`scipy` → dataset pipeline |
| `~/pytorch_test_env/` | PyTorch experimentation | `torch` → `accelerate`; `huggingface-cli` → models; `ollama` local compare |
| `~/quantum/` | Quantum mechanics / QED / QFT / sensing | `sympy`/`mpmath` → symbolic QM; `scipy` → numerical; `MEEP` → photonic cavity; `Wolfram` → cross-check; `openEMS` → EM field sim |
| `~/tec-scope/` | Z80 telescope mount controller | Z80 ASM → `sdcc` → RC2014/TEC-1; `arduino-cli` → ATtiny84/85 encoder; `sigrok` + `fx2lafw` → SPI/UART decode; `pyserial` → Stellarium comms; `matplotlib` → position plots |
| `~/robots/` | Physical robot builds | ROS2 full stack; `FreeCAD` → mechanical design → CNC; `pybullet` (Python) → simulation; `pyvisa`/`pymeasure` → bench test actuators |
| `~/ros/` `~/ros2/` | ROS middleware | ROS2 (`rclpy`, `ros2launch`, `ros2bag`, `tf2`) → full robot comms stack |
| `~/soma/ros/` | SOMA ROS2 integration | ROS2 + `torch` inference + `pyserial` hardware |
| `~/z80/` | Z80 assembly / RC2014 / TEC-1 | Z80 ASM → `sdcc` → `cap32` (emulate) → RC2014 flash |
| `~/mint/` | MINT language / TEC-1 / Octave | `Octave` → MINT-Octave cross-sim; Z80 ASM → `sdcc` → TEC-1; `cap32` → CPC emulation; `matplotlib` → Lorenz/fractal plots |
| `~/Forth/` | Forth on CPC-464 / CP/M | `cap32` → CPC emulation; `sdcc` → Z80 code; Forth disk images (`.dsk`) |
| `~/cpc464/` | Amstrad CPC-464 hardware | `cap32` emulator; `sdcc` C → Z80; USB floppy interface |
| `~/tec-chess/` | Chess AI on TEC-1 | Z80 ASM → `sdcc` → `cap32` (test) → TEC-1 flash |
| `~/cad/` | FreeCAD mechanical / FEA | `FreeCAD` → STL → MakeraCAM (CNC); `OpenSCAD` → parametric; Elmer FEM → structural/thermal |
| `~/blender/` | 3D modeling / rendering | `Blender` → STL → `FreeCAD`; `Blender` Python API → procedural geometry |
| `~/openEMS-Project/` | FDTD EM simulation framework | `openEMS` → `CSXCAD` → `h5py` → `matplotlib`; → VTK visualization; `scikit-rf` → S-params |
| `~/wolfram/` | Wolfram Language / symbolic math | `WolframKernel` → vector calculus; `sympy` cross-check; `mpmath` arbitrary precision |
| `~/maths/` | Mathematics reference library | `sympy` + `scipy` + `mpmath` + `Julia` + `Wolfram` — all math chains apply |
| `~/nn/` | Neural network theory / research | `torch` → experiments; `numpy`/`scipy` → from-scratch implementations; `networkx` → topology |
| `~/brain/` `~/brain/Predictive/` | Neuroscience / predictive coding | `torch` → predictive models; `numpy`/`scipy` → spike/rate coding; `networkx` → connectome graphs |
| `~/Rydberg_Atom_Electric_Field_Sensors_RAEFS/` | Rydberg atom quantum sensing | `MEEP` → cavity photonics; `openEMS` → RF field; `sympy`/`scipy` → atomic physics; `Wolfram` → analytical |
| `~/rockets/` | Aerospace / rocketry | `FreeCAD` → body design → CNC; `openEMS` → RF (telemetry antennas); `scipy` → trajectory sim; `matplotlib` → plots |
| `~/quantum/exp1-3/` `~/quantum/rtd/` | Quantum experiments / RTD | `ngspice`/`PySpice` → RTD tunnel junction sim; `lcapy` → symbolic circuit; `pyvisa` → lab instrument |
| `~/Cascaded-Modulator-Ising-Machine-CMIM/` | Ising machine / analog computing | `MEEP` → modulator FDTD; `ngspice` → electronic model; `sympy`/`scipy` → Ising Hamiltonian; `openEMS` → EM coupling |
| `~/Thermal_Stochastic_Computing/` | Thermal noise computing | `ngspice`/`PySpice` → thermal noise SPICE; `sympy` → stochastic analysis; `scipy` → Langevin sim; `matplotlib` → noise plots |
| `~/whisper.cpp/` | Local speech-to-text | `ffmpeg` → audio prep → `whisper.cpp`; `sox` → format convert; `pyserial` → mic input |
| `~/astro_siril/` | Astrophotography image processing | `PIL`/`opencv-python` → image pipeline; `scipy` → stacking/alignment; `matplotlib` → result plots |
| `~/vtk-src/` `~/vtk-build/` | VTK visualization library | VTK → `openEMS` field viz; `matplotlib` fallback; `h5py` → data load |
| `~/tinyml/` SOMA→ESP32 | SOMA cognitive stack → embedded | `torch` → quantize → TFLite → `arduino-cli` → ESP32; `pyserial` → runtime comms |
| `~/bitnet1.58/` | 1-bit neural network research | `torch` → custom kernels; `numpy` → bit manipulation; `huggingface-cli` → base models |
| `~/voxCAD/` | Voxel-based CAD | `FreeCAD` → export; `OpenSCAD` → voxel geometry; `Blender` → mesh conversion |
| `~/3D Gaussian Splatting/` | Neural 3D reconstruction | `torch` → 3DGS training; `opencv-python` → image input; `matplotlib`/`Blender` → visualization |
