# ADR 0006: Optional browser Git playground

[English](0006-browser-playground.md) · [Português](0006-browser-playground.pt-BR.md) · [Español](0006-browser-playground.es.md)

Status: proposed in Sprint 18, documentation-based evaluation on 2026-11-27; defer runtime adoption.

## Decision

Keep all native practical projects and challenges local_only. Other chapters remain unverified. No browser_compatible capability, package, public proxy, server, runtime version or deployment approved. A browser tool is optional and must not replace the native Git reference or be required to complete any learning path.

## Alternatives

| Alternative | Evidence and limitations | Decision |
| --- | --- | --- |
| Native Git in disposable local repositories | Existing Linux/Windows tests cover real index, refs, conflicts, reflog, bare origins and recovery. No browser UI; learners install Git. | Reference implementation |
| isomorphic-git | JavaScript Git implementation with browser filesystem and HTTP adapters; documented add, commit, branch, checkout, merge, cherry-pick, stash and tag APIs. Its CLI is not a native Git CLI replacement; CORS and filesystem durability are constraints. Exact flags, state semantics and conflict/recovery parity unverified. | Candidate only |
| wasm-git | libgit2 compiled with Emscripten; documented browser builds include worker-based and persistent filesystem variants. CORS, build-specific storage/browser requirements and different implementation from Git CLI constrain fidelity. Pthreads OPFS needs cross-origin isolation headers. | Candidate only |
| Educational simulator | Could model a small state machine without claiming native Git; would need original explicit rules, clear simulation labeling and native comparison fixtures. | Optional future exploration |
| Server-hosted arbitrary Git shell | Introduces execution isolation, network/security risk and uncertain recurring cost. | Rejected |

## Required prototype gates before any capability change

- Pin exact package/runtime versions, dependency licenses and integrity hashes. Bundle static assets without mandatory accounts, public CORS proxies, paid infrastructure or per-visitor API calls. Verify actual hosting/bandwidth limits before approval.
- Start with a small offline disposable fixture and typed allowlisted operations (init, status, add, commit, branch/checkout, diff). Compare working/index/HEAD bytes and graph/state against native Git, then expand only after testing conflicts, stash, revert, squash, reflog, tags and local bare-remote simulation. Never infer support from API names. Unsupported operations remain local_only.
- Separate site and runtime origins where necessary; enforce CSP and restrictive messaging, no credentials, arbitrary shell, unrestricted networking or access to valuable repositories. A Web Worker improves responsiveness but alone is not a security boundary. Inspect dependency supply chain and origin isolation.
- Proposed test limits, not measured guarantees: 5 s per operation, 64 KiB output, 5 MiB fixture, 100 operations per session. Cancel/terminate and recreate workers; no claim of hard browser memory isolation. Test quota errors, crash/reload, cleanup and reset; storage can be evicted, so export/restart guidance and explicit opt-in persistence are required.
- Verify keyboard-only operation, screen reader labels, localized errors, contrast, focus, mobile layout, reduced motion and Chrome/Edge/Firefox/Safari on target devices. Test offline use, version pinning, CORS/network denial, state reset, time/output caps and recovery. Document actual results per exercise before marking browser_compatible in a future version.

## Consequences

No new cost or dependency is introduced here. No live browser/runtime test or compatibility claim; the assessment is based on documentation, not a benchmark. Future site-side prototype requires separate authorization, measured fidelity, security/accessibility review and confirmed zero additional cost. Local labs remain fully available without it.

## Sources consulted

- <https://github.com/isomorphic-git/isomorphic-git/blob/main/README.md>
- <https://isomorphic-git.org/docs/en/quickstart>
- <https://github.com/petersalomonsen/wasm-git/blob/master/README.md>
- <https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers>
- <https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria>
- <https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy>
- <https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/sandbox>

- [Integration contract](../specs/project-foundation/integration-contract.md)
- [ADR index](README.md)
