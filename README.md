# Brick Knowledge Graph Builder

## Description

This project builds a Neo4j knowledge graph focused on the topic of "Bricks". It extracts information from specific textual sources related to brick history, materials, construction techniques, and conservation practices, structuring this data into a graph database.

## Features

*   Connects to a Neo4j database.
*   Creates a central "Topic" node (e.g., "BRICKS").
*   Parses information from different sources (`satish_chandra.py`, `tatatrust.py`) representing books or documents.
*   Creates nodes for Books, Chapters, Sections, Subsections, and References.
*   Establishes relationships between these nodes (e.g., `HAS_BOOK`, `HAS_CHAPTER`, `HAS_SECTION`, `HAS_SUBSECTION`, `CITES`) to represent the structure and connections within the knowledge domain.

## Prerequisites

*   Python 3.x
*   pip (Python package installer)
*   A running Neo4j instance (Server or Desktop).

## Installation

1.  **Clone the repository (if applicable) or ensure you have the project files.**
2.  **Navigate to the project directory:**
    ```bash
    cd "Knowledge-graph-rag"
    ```
3.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  Open the `main.py` file.
2.  Update the Neo4j connection details if they differ from the defaults:
    *   `uri`: Your Neo4j Bolt URI (e.g., `"bolt://localhost:7687"`)
    *   `user`: Your Neo4j username (e.g., `"neo4j"`)
    *   `password`: Your Neo4j password.

## Usage

1.  **Ensure your Neo4j server is running.**
2.  **Run the main script from the project directory:**
    ```bash
    python main.py
    ```
    This will connect to the Neo4j database and populate it with the nodes and relationships defined in the `satish_chandra.py` and `tatatrust.py` modules.

## Project Structure

```
.
├── main.py             # Main script to run the knowledge graph creation process.
├── knowledge_graph.py  # Class definition for interacting with the Neo4j database.
├── satish_chandra.py   # Module to extract and structure data from the first source.
├── tatatrust.py        # Module to extract and structure data from the second source.
└── requirements.txt    # List of Python dependencies.
```

## Knowledge Graph Schema

The script creates the following node labels and relationship types:

*   **Nodes:**
    *   `Topic`: Represents the main subject (e.g., "BRICKS").
    *   `Book`: Represents a source document.
    *   `Chapter`: Represents a chapter within a book.
    *   `Section`: Represents a section within a chapter.
    *   `Subsection`: Represents a subsection within a section.
    *   `Subsubsection`: Represents a subsubsection within a subsection.
    *   `Reference`: Represents a cited reference.
*   **Relationships:**
    *   `HAS_BOOK`: Connects a `Topic` to a `Book`.
    *   `HAS_CHAPTER`: Connects a `Book` to a `Chapter`.
    *   `HAS_SECTION`: Connects a `Chapter` to a `Section`.
    *   `HAS_SUBSECTION`: Connects a `Section` to a `Subsection`.
    *   `HAS_SUBSUBSECTION`: Connects a `Subsection` to a `Subsubsection`.
    *   `CITES`: Connects a `Section` (or other content node) to a `Reference`.

You can explore the generated graph using the Neo4j Browser or Bloom.
