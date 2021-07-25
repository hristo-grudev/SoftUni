class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category in self.categories:
            return
        self.categories.append(category)

    def add_topic(self, topic):
        if topic in self.topics:
            return
        self.topics.append(topic)

    def add_document(self, document):
        if document in self.documents:
            return
        self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = [c for c in self.categories if c.id == category_id][0]
        category.name = new_name
        return

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = [c for c in self.topics if c.id == topic_id][0]
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder
        return

    def edit_document(self, document_id, new_file_name):
        document = [c for c in self.documents if c.id == document_id][0]
        document.file_name = new_file_name
        return

    def delete_category(self, category_id):
        category = [c for c in self.categories if c.id == category_id][0]
        if category:
            self.categories.remove(category)
        return

    def delete_topic(self, topic_id):
        topic = [t for t in self.topics if t.id == topic_id][0]
        if topic:
            self.topics.remove(topic)
        return

    def delete_document(self, document_id):
        document = [d for d in self.documents if d.id == document_id][0]
        if document:
            self.documents.remove(document)
        return

    def get_document(self, document_id):
        document = [c for c in self.documents if c.id == document_id][0]
        return document

    def __repr__(self):
        string = '\n'.join([d.__repr__() for d in self.documents])
        return string
