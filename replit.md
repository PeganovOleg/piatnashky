# 3D Cube Visualization Application

## Overview

This is a full-stack web application built with React, TypeScript, and Express that provides an interactive 3D cube visualization experience. The application features a React Three Fiber-based 3D scene with customizable cube controls, audio integration, and a modern UI built with Radix UI components and Tailwind CSS.

## System Architecture

### Frontend Architecture
- **Framework**: React 18 with TypeScript
- **3D Rendering**: React Three Fiber (@react-three/fiber) with Three.js
- **3D Utilities**: React Three Drei (@react-three/drei) for common 3D components
- **State Management**: Zustand for global state management
- **UI Components**: Radix UI primitives with shadcn/ui styling
- **Styling**: Tailwind CSS with custom CSS variables for theming
- **Build Tool**: Vite with custom configuration for 3D assets

### Backend Architecture
- **Framework**: Express.js with TypeScript
- **Development Server**: Custom Vite integration for hot reloading
- **Database ORM**: Drizzle ORM configured for PostgreSQL
- **Session Management**: Prepared for connect-pg-simple integration
- **API Structure**: RESTful endpoints with middleware for logging and error handling

### Database Schema
- **ORM**: Drizzle ORM with PostgreSQL dialect
- **Connection**: Neon Database serverless connection
- **Schema Definition**: Centralized in `shared/schema.ts`
- **Current Tables**: Users table with basic authentication fields
- **Migrations**: Managed through Drizzle Kit

## Key Components

### 3D Visualization System
- **CubeVisualization**: Main 3D scene component with interactive cube
- **CubeControls**: UI overlay for controlling cube properties (rotation, wireframe, scale)
- **OrbitControls**: Camera manipulation for user interaction
- **Lighting Setup**: Ambient, directional, and point lights for realistic rendering

### State Management
- **useGame**: Game phase management (ready, playing, ended)
- **useAudio**: Audio control system with background music and sound effects
- **Component State**: Local state for 3D object properties and animations

### UI System
- **Responsive Design**: Mobile-first approach with adaptive controls
- **Theme System**: Dark mode with CSS custom properties
- **Component Library**: Comprehensive UI components from Radix UI
- **Keyboard Controls**: Spacebar for play/pause, additional hotkeys for cube manipulation

## Data Flow

### 3D Rendering Pipeline
1. React Three Fiber canvas initialization
2. Scene setup with lighting and camera configuration
3. Cube mesh creation with material properties
4. Animation loop using useFrame hook
5. User interaction handling through event system

### State Updates
1. User interactions trigger state updates in Zustand stores
2. Component re-renders based on state changes
3. 3D scene updates through React Three Fiber's reconciliation
4. Audio system responds to game state changes

### API Communication
- **Client-Server**: Prepared for RESTful API calls using fetch
- **Query Management**: TanStack Query for data fetching and caching
- **Error Handling**: Centralized error boundary system

## External Dependencies

### Core Libraries
- **React Ecosystem**: React, React DOM, React Three Fiber
- **3D Graphics**: Three.js, React Three Drei, React Three Postprocessing
- **Database**: Drizzle ORM, Neon Database serverless driver
- **UI Framework**: Radix UI primitives, Tailwind CSS
- **State Management**: Zustand with subscriptions
- **Build Tools**: Vite, ESBuild, TypeScript

### Development Tools
- **Hot Reloading**: Custom Vite setup with runtime error overlay
- **Asset Handling**: GLSL shader support, GLTF/GLB model loading
- **Code Quality**: TypeScript strict mode, ESLint configuration

## Deployment Strategy

### Production Build
- **Frontend**: Vite build optimization with asset bundling
- **Backend**: ESBuild compilation for Node.js environment
- **Database**: Drizzle migrations with environment-specific configurations
- **Deployment Platform**: Replit with autoscale deployment target

### Environment Configuration
- **Development**: Local development with hot reloading
- **Production**: Optimized builds with asset compression
- **Database**: Environment-specific connection strings
- **Port Management**: Configurable port mapping (5000 internal, 80 external)

### Performance Optimizations
- **3D Rendering**: High-performance GPU preferences
- **Asset Loading**: Lazy loading for 3D models and textures
- **Code Splitting**: Dynamic imports for large components
- **Caching**: Browser and server-side caching strategies

## Changelog

Changelog:
- June 21, 2025. Initial setup
- June 21, 2025. Created 3D cube visualization program with React Three Fiber
- June 21, 2025. User successfully downloaded the project code
- June 21, 2025. Created Hearts Puzzle game (15-puzzle with hearts) in Python
- June 21, 2025. Created web version of Hearts Puzzle with blue hearts instead of pink
- June 21, 2025. Added navigation link to Hearts Puzzle in main 3D app - user confirmed working
- June 21, 2025. Enhanced Hearts Puzzle: changed to blue hearts, added numbers 1-15, increased sizes per user request
- June 21, 2025. Final improvements: made hearts bigger (80px), lighter blue colors, larger text (18px), added complete timer functionality that tracks time from first move to victory
- June 21, 2025. Added pleasant click sound effects using Web Audio API for tile movements and victory sounds - user confirmed working
- June 21, 2025. Fully adapted for mobile devices: responsive design, touch controls, viewport optimization, eliminated scroll issues, improved touch targets

## User Preferences

Preferred communication style: Simple, everyday language.
Preferred language: Russian
Enjoys games and visual applications
Prefers blue color scheme for hearts over pink/red