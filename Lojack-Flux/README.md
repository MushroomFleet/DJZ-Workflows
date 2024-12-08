# LojackFlux Workflow Pack

A collection of advanced Flux-based workflows implementing ComfyUI's masking and scheduling systems, enhanced with custom motion masks and prompt management systems.

**Repository**: [DJZ-Workflows/Lojack-Flux](https://github.com/MushroomFleet/DJZ-Workflows/tree/main/Lojack-Flux)

## Overview

This workflow pack adapts ComfyUI's masking and scheduling capabilities for the Flux1 Schnell pipeline, providing powerful tools for creating complex image generations with precise control over LoRA application and model weights.

### Included Workflows

1. **LojackFlux-Mask**
   - Implements dynamic masking system with custom motion masks
   - Supports black/white geometric pattern videos for mask generation
   - Integrated directory index selector for motion mask management
   - Frame selection support for both still images and animation sequences

![LojackFlux-Mask Workflow](https://raw.githubusercontent.com/MushroomFleet/DJZ-Workflows/main/Lojack-Flux/images/Lojack-Flux-Mask.png)

2. **LojackFlux-Schedule**
   - Enables temporal control over LoRA and model weight application
   - Perfect for creating smooth transitions between different styles or models

![LojackFlux-Schedule Workflow](https://raw.githubusercontent.com/MushroomFleet/DJZ-Workflows/main/Lojack-Flux/images/Lojack-Flux-scheduling.png)

3. **LojackFlux-ComboBreaker**
   - Combines both masking and scheduling capabilities
   - Allows for complex, multi-stage image generation with precise control

![LojackFlux-ComboBreaker Workflow](https://raw.githubusercontent.com/MushroomFleet/DJZ-Workflows/main/Lojack-Flux/images/lojack-flux-ComboBreaker.png)

## Key Features

### Custom Integration Systems
- **Zenkai Prompt List**: Streamlined prompt management system
- **Project File Path System**: Organized file handling and output management
- **Motion Mask System**: 
  - Directory-based mask selection
  - Frame-specific control
  - Support for both static and animated outputs
  - Motion mask assets available at: [Lonely-Drivers-Pack](https://huggingface.co/mushroomfleet/Lonely-Drivers-Pack)

### Masking System
The masking system allows you to:
- Apply different LoRAs to specific areas of your image
- Blend multiple model weights across different regions
- Use dynamic motion masks for complex pattern generation
- Automatically handle unmapped regions to prevent artifacts

### Scheduling System
Enables precise control over:
- Temporal application of LoRAs
- Model weight transitions
- Strength adjustment over time
- Integration with motion mask animations

## Animation Features & Interpolation

### Frame Interpolation Tool
![Interpolation Tool Preview](https://raw.githubusercontent.com/MushroomFleet/DJZ-Workflows/main/Lojack-Flux/images/lojack-interp-tool.png)

The workflow pack includes a specialized interpolation tool designed for enhancing animation sequences. This tool provides:

- **Anti-Flicker Processing**: Built-in mechanisms to reduce unwanted flickering between frames
- **Smooth Transitions**: Intelligent frame interpolation for fluid motion
- **Batch Processing**: Handle entire animation sequences efficiently
- **Frame Rate Control**: Flexible FPS adjustment for output animations
- **Quality Control**: Balance between interpolation quality and processing speed

The interpolation system works seamlessly with both the masking and scheduling workflows, allowing you to:
- Smooth out transitions between different LoRA applications
- Reduce artifacts in mask-based animations
- Create more natural motion from scheduled weight changes
- Process multiple animation segments with consistent quality

This tool is particularly useful when:
- Creating long animation sequences
- Working with motion mask transitions
- Combining multiple style changes in a single animation
- Converting frame sequences to smooth video outputs

## Technical Details

### Conditioning System
- Supports multiple conditioning pairs (positive/negative)
- Automatic mask validation and combination
- Default conditioning fallback for unmapped areas
- Compatible with additional control methods (ControlNet, etc.)

### Weight Management
- Dynamic LoRA strength control
- Model weight interpolation
- Support for multiple concurrent LoRAs
- Automatic CLIP and model weight handling

## Usage Tips

![Lonely Drivers Motion Mask Examples](https://raw.githubusercontent.com/MushroomFleet/DJZ-Workflows/main/Lojack-Flux/images/lonely-drivers.gif)

1. **Installation**
   - Clone or download from: [https://github.com/MushroomFleet/DJZ-Workflows/tree/main/Lojack-Flux](https://github.com/MushroomFleet/DJZ-Workflows/tree/main/Lojack-Flux)
   - Place workflows in your ComfyUI workflows directory

2. **Mask Generation**
   - Download motion masks from the [Lonely-Drivers-Pack repository](https://huggingface.co/mushroomfleet/Lonely-Drivers-Pack)
   - Use black/white video patterns for dynamic masks
   - Ensure complete coverage when using multiple masks
   - Utilize default conditioning for unmapped areas

3. **Scheduling**
   - Plan your weight transitions carefully
   - Use gradual strength adjustments for smooth results
   - Combine with motion masks for dynamic effects

4. **File Management**
   - Organize motion masks in the designated directory
   - Use the Zenkai Prompt List for consistent results
   - Follow the project file path structure for outputs

## Requirements

- Flux1 Schnell pipeline
- ComfyUI latest version
- Properly structured motion mask directory
- Compatible LoRA models
- Motion mask assets from Lonely-Drivers-Pack

## Notes

- Based on ComfyUI's native masking and scheduling system
- Optimized specifically for Flux1 Schnell pipeline
- Compatible with all standard Stable Diffusion models
- Enhanced with custom motion mask integration

## Resources

- **Workflow Pack**: https://github.com/MushroomFleet/DJZ-Workflows/tree/main/Lojack-Flux
- **Motion Masks**: https://huggingface.co/mushroomfleet/Lonely-Drivers-Pack

## Motion Mask Examples



## Credits

Original ComfyUI masking and scheduling system adapted for Flux pipeline with additional custom features and integrations.
Motion masks provided by the Lonely-Drivers-Pack.
