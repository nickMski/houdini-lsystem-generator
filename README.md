# Procedural Growth System for Houdini

A sophisticated procedural growth system implemented in Houdini, combining L-Systems with environmental awareness and physical growth behaviors. This tool enables the creation of naturally growing structures that respond to environmental factors like light, space availability, and noise influences.

## Features

- L-System based procedural growth with customizable rules
- Environmental awareness including:
  - Light influence with height-based calculations
  - Space availability checking
  - Noise-based variation
- Configurable growth parameters:
  - Branch angles
  - Segment lengths
  - Growth iterations
  - Environmental influence factors
- Real-time parameter adjustments through Houdini's interface

## Technical Implementation

The system consists of two main components:

1. **Python-based L-System Parser:**
   - Object-oriented implementation of an L-System interpreter
   - Stack-based branch management
   - Quaternion-based rotation handling

2. **VEX-based Growth Solver:**
   - Environmental factor calculation
   - Dynamic growth direction computation
   - Age-based color attribution

## Installation

1. Clone this repository into your Houdini project directory:
```bash
git clone https://github.com/yourusername/houdini-procedural-growth.git
```

2. In Houdini, create a new Digital Asset and copy the contents of the Python and VEX scripts into their respective sections.

## Usage

L-System Tree Generation Parameters
Python Node Parameters

iterations (Growth Iterations)

Controls L-system string complexity
More iterations = more complex branching structure
Code impact: for _ in range(iterations) expands initial axiom


angle (Branch Angle)

Defines rotation angle for branching
Controls how sharply branches deviate
VEX impact: Rotation matrix in branch generation


length (Segment Length)

Determines distance between points
Directly scales distance of line segments
VEX impact: pos + dir * length



Point Wrangle Parameters (VEXpression)

light_influence

Controls how much vertical growth is influenced by light
Blends growth direction towards vertical axis
VEX: lerp(current_dir, up, light * light_influence)


space_check_radius

Defines neighborhood search radius
Determines crowding detection
VEX: nearpoints(0, pos, space_check_radius)


max_neighbors

Maximum point count in search radius
Influences growth crowding factor
VEX: Calculates crowd density relative to this value


noise_freq

Controls noise pattern frequency
Affects randomness of growth direction
VEX: curlnoise(pos * noise_freq)


noise_amount

Scales noise influence on growth
Determines randomness intensity
VEX: noise_offset * noise_amount


growth_rate

Base growth speed
Multiplies overall growth movement
VEX: Directly scales point position change


light_noise_freq

Noise frequency for light interactions
Adds variation to light-based growth
VEX: noise(pos * light_noise_freq)


time

Temporal offset for growth
Enables animation/dynamic growth
VEX: Used in noise calculations for temporal variation
