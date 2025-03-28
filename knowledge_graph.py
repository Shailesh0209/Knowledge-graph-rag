from neo4j import GraphDatabase

class KnowledgeGraph:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        self.driver.close()
    
    def create_node(self, label, properties):
        query = f"CREATE (n:{label} $props) RETURN id(n) as node_id"
        with self.driver.session() as session:
            result = session.run(query, props=properties)
            node_id = result.single()["node_id"]
            return node_id

    def create_relationship(self, start_id, rel_type, end_id):
        query = (
            "MATCH (a), (b) "
            "WHERE id(a)=$start_id AND id(b)=$end_id "
            f"CREATE (a)-[r:{rel_type}]->(b) "
            "RETURN r"
        )
        with self.driver.session() as session:
            session.run(query, start_id=start_id, end_id=end_id)

    # Helper functions to create specific node types
    def create_topic(self, name):
        return self.create_node("Topic", {"name": name})
    
    def create_book(self, title, description=""):
        return self.create_node("Book", {"title": title, "description": description})
    
    def create_chapter(self, title, summary=""):
        return self.create_node("Chapter", {"title": title, "summary": summary})
    
    def create_section(self, title, content=""):
        return self.create_node("Section", {"title": title, "content": content})
    
    def create_subsection(self, title, content=""):
        return self.create_node("Subsection", {"title": title, "content": content})
    
    def create_subsubsection(self, title, content=""):
        return self.create_node("Subsubsection", {"title": title, "content": content})
    
    def create_reference(self, citation, details=""):
        properties = {"citation": citation, "details": details}
        return self.create_node("Reference", properties)