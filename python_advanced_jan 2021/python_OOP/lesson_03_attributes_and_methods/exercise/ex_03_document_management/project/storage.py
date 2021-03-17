class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        res = '\n'.join([d.__repr__() for d in self.documents])
        return res

    def get_category_by_id(self, category_id):
        category = [category for category in self.categories if category_id == category.id][0]
        return category

    def get_topic_by_id(self, topic_id):
        topic = [topic for topic in self.topics if topic_id == topic.id][0]
        return topic

    def get_document(self, document_id):
        document = [document for document in self.documents if document_id == document.id][0]
        return document

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = self.get_category_by_id(category_id)
        category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.get_topic_by_id(topic_id)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = self.get_document(document_id)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.get_category_by_id(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.get_topic_by_id(topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.get_document(document_id)
        self.documents.remove(document)

