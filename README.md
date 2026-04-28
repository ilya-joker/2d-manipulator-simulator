# 2D Manipulator Simulator

A Python project for simulating a 2-link robotic manipulator.

The project includes forward kinematics, inverse kinematics, reachability checks, simple tests, and Matplotlib visualization.

## Features

- Forward kinematics: calculates joint and end-effector positions from link lengths and angles.
- Inverse kinematics: calculates joint angles for a given target point.
- Reachability check: detects whether a target point is reachable.
- Visualization with Matplotlib.
- Basic test scripts for checking forward and inverse kinematics.

## Project structure

```text
2d-manipulator-simulator/
├─ src/
│  └─ manipulator/
│     ├─ config.py
│     ├─ math_utils.py
│     ├─ forward_kinematics.py
│     ├─ inverse_kinematics.py
│     ├─ visualizer.py
│     ├─ printer.py
│     ├─ main.py
│     └─ main_reverse.py
├─ tests/
│  ├─ test_forward_kinematics.py
│  └─ test_inverse_kinematics.py
├─ requirements.txt
├─ .gitignore
└─ README.md