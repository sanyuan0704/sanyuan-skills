# Project Brain: Global Architecture Rules

> **Note to User**: Customize this file for each project. It defines the "non-negotiables" that the Code Review Expert must enforce regardless of general best practices. All sections are filled out with concrete, enforceable defaults, making this drop-in usable for new users and reducing AI hallucinations.

## Core Architecture Pattern
- **Pattern**: Hexagonal (Ports & Adapters) <!-- DEFAULT THAT CAN BE SWAPPED; suggested alternatives: Layered (MVC), Event-Driven -->
- **Constraint**: Business logic stays in `src/domain` with zero framework imports; frameworks live in `src/infrastructure` or `src/interface`. <!-- RULE THAT MUST STAY -->
- **Dependency Direction**: Outer layers may depend on inner layers; inner layers must not import outer code. <!-- RULE THAT MUST STAY -->

## Technical Stack & Versioning
- **Language/Runtime**: TypeScript 5.4 on Node.js 20.x <!-- DEFAULT THAT CAN BE SWAPPED; suggested alternatives: Python 3.12, Go 1.22 -->
- **Primary Libraries**:
    - **Validation**: Zod — all inbound API/queue payloads must be parsed via schemas in `src/interface/validation`. <!-- DEFAULT THAT CAN BE SWAPPED; alternatives: Joi, Yup; keep separation of validation layer -->
    - **Database**: Prisma — repositories live in `src/infrastructure/prisma`. <!-- DEFAULT THAT CAN BE SWAPPED; alternatives: TypeORM, Drizzle; RULE: infrastructure layer must handle DB -->
    - **HTTP**: Fastify — routes in `src/interface/http` call application services, never domain directly. <!-- DEFAULT THAT CAN BE SWAPPED; alternatives: Express, NestJS -->
    - **State Management (frontends)**: Zustand for SPA dashboards. <!-- DEFAULT THAT CAN BE SWAPPED; alternatives: Redux Toolkit, MobX -->
- **Forbidden Libraries**: Moment.js (use date-fns), `any`-heavy utils, `request` package, deprecated `uuid/v1`. <!-- RULE THAT MUST STAY -->

## Data & Persistence Laws
- **Ownership**: Services never cross-read databases; communicate via HTTP/async events only. <!-- RULE THAT MUST STAY -->
- **Migrations**: Must be backward compatible for one release; include down migrations and rollout notes. <!-- RULE THAT MUST STAY -->
- **Soft Deletes**: Use `deleted_at TIMESTAMP NULL` columns; no hard deletes of user data. <!-- RULE THAT MUST STAY -->

## Error & Communication Standards
- **Error Registry**: All domain/app errors extend `AppError` with fields `{ code, message, httpStatus, details? }`; codes use `DOMAIN_CONTEXT_ERROR` (e.g., `AUTH_INVALID_TOKEN`). <!-- RULE THAT MUST STAY -->
- **Async Patterns**: Prefer `async/await`; wrap top-level handlers with `withErrorBoundary(handler)` to log and map errors to HTTP responses. <!-- RULE THAT MUST STAY -->
- **Event Naming**: `Resource.Action.Status` with past-tense action (e.g., `Order.Created.Success`, `User.PasswordReset.Requested`); events are JSON, versioned via `meta.schemaVersion`. <!-- RULE THAT MUST STAY -->

## Testing Philosophy
- **Standard**: TDD on services, behavioral tests on routes/handlers. <!-- DEFAULT THAT CAN BE SWAPPED; alternatives: Behavioral-only, BDD -->
- **Coverage**: >=80% line coverage overall; 100% on auth/payments modules. <!-- DEFAULT THAT CAN BE SWAPPED; can adjust percentages for smaller projects -->
- **Mocking**: Only mock third-party APIs; database tests run on testcontainers-based Postgres. <!-- RULE THAT MUST STAY for consistency -->

## The "Wall of Shame" (Project Anti-Patterns)
- No "God Objects" in `src/utils`. <!-- RULE THAT MUST STAY -->
- Avoid `any`; prefer `unknown` + narrowing. <!-- RULE THAT MUST STAY -->
- Do not use `console.log`; use `Logger` with structured fields. <!-- RULE THAT MUST STAY -->