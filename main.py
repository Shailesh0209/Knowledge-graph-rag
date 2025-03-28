from knowledge_graph import KnowledgeGraph
from satish_chandra import create_book as create_book1
from tatatrust import create_book as create_book2

def main():
    # Connection details for Neo4j
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "17021702"  # Use your actual password

    kg = KnowledgeGraph(uri, user, password)
    try:
        # Create a root topic node (if applicable)
        topic_id = kg.create_topic("BRICKS")
        
        # Create Book 1
        book1_id = create_book1(kg, topic_id)
        
        # Create Book 2
        book2_id = create_book2(kg, topic_id)
        
    finally:
        kg.close()

if __name__ == "__main__":
    main()
