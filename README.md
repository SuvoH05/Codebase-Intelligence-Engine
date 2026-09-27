# Codebase Intelligence Engine

A local-first AI system for understanding and navigating codebases. Instead of relying on exact keyword search, it lets you ask natural-language questions about a repository — like *"where is authentication handled?"* — and get relevant code back.

## Status

🚧 **Early development.** Currently working on the file-reading / repository-loading stage of Phase 1. Not yet functional end-to-end.

## Vision

An assistant that can:
- Understand a repository's codebase
- Retrieve relevant code for a given question
- Explain how parts of the architecture work
- Trace bugs across files
- Help developers navigate and modify large codebases more efficiently

## Planned Architecture

### Phase 1 — Pure Semantic MVP
- Load repositories from disk
- Split code into meaningful chunks (files / functions / classes)
- Generate embeddings for each chunk
- Store embeddings in a vector database (Chroma or FAISS)
- Enable semantic search over the codebase, without needing exact keyword matches

### Unified Indexing Layer
- A single indexer produces stable IDs shared across both vector chunks and (future) graph nodes
- Keeps the semantic view (embeddings) and the structural view (graph) in sync as the codebase changes

### Phase 2 — Hybrid Graph Intelligence
- Use Tree-sitter to parse code and extract symbols, imports, classes, functions, and relationships
- Build an in-memory graph layer on top of this structure
- Answer structural questions: dependencies, call flows, impact analysis

## Tech Stack (planned)

- **Language:** Python
- **Embeddings / Vector DB:** Chroma or FAISS
- **Parsing:** Tree-sitter
- **Design principle:** Local-first — no code leaves your machine

## Roadmap

- [ ] Repository loading / file reading
- [ ] Chunking strategy (file / function / class level)
- [ ] Embedding generation
- [ ] Vector store integration
- [ ] Semantic search interface
- [ ] Unified indexer with stable IDs
- [ ] Tree-sitter based symbol extraction
- [ ] In-memory code graph
- [ ] Structural queries (dependencies, call flow, impact analysis)

## Contributing

This project is in very early stages — not yet open for contributions, but suggestions and ideas are welcome.

## License

TBD
