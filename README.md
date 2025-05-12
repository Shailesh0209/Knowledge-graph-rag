# Brick Conservation Knowledge Graph

## Project Overview
This project implements a knowledge graph for historical brick conservation literature, designed to organize, connect, and make searchable complex information about traditional brick-making techniques and conservation practices across India. Using Neo4j as the graph database, it transforms unstructured text from authoritative sources into a structured, queryable knowledge base.

## Key Features
- **Hierarchical Organization**: Content structured as Topic → Book → Chapter → Section → Subsection → Subsubsection
- **Relationship Mapping**: Explicit connections between related concepts (e.g., citation relationships)
- **Multi-source Integration**: Combines information from multiple sources (Satish Chandra's historical text and Tata Trust's conservation specifications)
- **Extensible Framework**: Can be expanded with additional sources or embedding capabilities

## Knowledge Graph Structure

### Node Types
- **Topic**: Root-level domain (e.g., "BRICKS")
- **Book**: Literary sources containing brick-related information
- **Chapter**: Major divisions within books
- **Section**: Sub-divisions of chapters
- **Subsection**: Detailed content areas
- **Subsubsection**: Specific techniques or concepts
- **Reference**: Citations and bibliographic information

### Relationship Types
- **HAS_BOOK**: Connects Topic to Books
- **HAS_CHAPTER**: Connects Books to Chapters
- **HAS_SECTION**: Connects Chapters to Sections
- **HAS_SUBSECTION**: Connects Sections to Subsections
- **HAS_SUBSUBSECTION**: Connects Subsections to Subsubsections
- **CITES**: Connects content nodes to Reference nodes

## Technical Implementation

### Architecture
The project follows a modular design with separate components:
- Core graph database connector (`knowledge_graph.py`)
- Content modules (`satish_chandra.py`, `tatatrust.py`)
- Main script (`main.py`) that orchestrates graph creation

### Data Sources
1. **Historical Text**: "History of Architecture and Ancient Building Materials in India" by Satish Chandra
   - Contains historical context of brick usage in ancient India
   - Details traditional manufacturing techniques
   - Provides archaeological evidence from sites like Mohenjo-Daro and Dholavira

2. **Conservation Manual**: "Tata Trust Specifications for Built Heritage Conservation"
   - Modern conservation techniques for historic brick structures
   - Material specifications and handling instructions
   - Step-by-step repair methods for various brick defects

## Prerequisites
- Python 3.7+
- Neo4j Graph Database (local or cloud instance)
- Neo4j Python driver (`pip install neo4j`)

## Setup and Installation
1. Clone the repository
2. Install dependencies: `pip install neo4j`
3. Configure Neo4j connection in `main.py`:
   ```python
   uri = "bolt://localhost:7687"  # Update if using cloud instance
   user = "neo4j"                 # Your Neo4j username
   password = "your_password"     # Your Neo4j password
   ```

## Usage
```bash
cd Brick/kg_code
python main.py
```

## Potential Extensions
- **Semantic Search**: Add vector embeddings for content-based similarity search
- **Question Answering**: Build RAG (Retrieval Augmented Generation) applications on top of the graph
- **Interactive Visualization**: Develop a front-end to navigate the knowledge graph
- **Additional Sources**: Incorporate more texts on brick conservation from different regions

## Application Areas
- Heritage conservation planning
- Training conservationists and architects
- Documentation of traditional techniques
- Supporting restoration projects with historical context






