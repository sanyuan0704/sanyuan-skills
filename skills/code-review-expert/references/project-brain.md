# Project Brain: Global Architecture Rules

> **Note to User**: Customize this file for each project. It defines the "non-negotiables" that the Code Review Expert must enforce regardless of general best practices.

## Core Architecture Pattern
- **Pattern**: [e.g., Hexagonal, Layered (MVC), Microservices, Event-Driven]
- **Constraint**: "Business logic must remain in `src/domain` and have zero dependencies on frameworks (e.g., Express, NestJS)."
- **Dependency Direction**: "Outer layers (Infrastructure) can depend on Inner layers (Domain), but never the reverse."

## Technical Stack & Versioning
- **Language/Runtime**: [e.g., TypeScript 5.4 / Node.js 20.x]
- **Primary Libraries**:
    - **Validation**: [e.g., Zod] - "All API inputs must be parsed via Zod schemas."
    -**Database**: [e.g., Prisma / Drizzle / TypeORM]
    **State Management**: [e.g., Redux Toolkit / Zustand]
- **Forbidden Libraries**: [e.g., "Do not use Moment.js; use date-fns."]

## Data & Persistence Laws
- **Ownership**: "Services must never access another service's database directly. Use API/Events."

- **Migrations**: "Schema changes must always be backward compatible for at least one release."

- **Soft Deletes**: "We use `deleted_at` timestamps; never perform hard `DELETE` operations on user data."

## Error & Communication Standards
- **Error Registry**: "All custom errors must extend `AppError` and include a unique `errorCode`."
- **Async Patterns**: "Prefer `async/await` over `.then()`. All top-level async calls must be wrapped in a specific Error Boundary."
- **Event Naming**: "Events must follow the `Resource.Action.Status` pattern (e.g., `Order.Created.Success`)."

## Testing Philosophy
- **Standard**: [e.g., TDD / Behavioral]
- **Coverage**: "Maintain 80% line coverage. Critical paths (Auth/Payments) require 100%."
- **Mocking**: "Only mock external third-party APIs. Databases should be tested via test-containers or memory-db."

## The "Wall of Shame" (Project Anti-Patterns)
- "No 'God Objects' allowed in `src/utils`."
- "Avoid any type at all costs; use `unknown` if a type is truly dynamic."
- "Do not use `console.log`; use the internal `Logger` service."