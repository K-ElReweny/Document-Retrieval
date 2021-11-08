
class Retrieve:
    
    # Create new Retrieve object storing index and term weighting 
    # scheme. (You can extend this method, as required.)
    def __init__(self,index, term_weighting):
        self.index = index
        self.term_weighting = term_weighting
        self.num_docs = self.compute_number_of_documents()
        
    def compute_number_of_documents(self):
        self.doc_ids = set()
        for term in self.index:
            self.doc_ids.update(self.index[term])
        return len(self.doc_ids)

    # Method performing retrieval for a single query (which is 
    # represented as a list of preprocessed terms). Returns list 
    # of doc ids for relevant docs (in rank order).
    def for_query(self, query):
        if self.term_weighting == 'binary':
          return self.binary_term_weight(query)
        elif self.term_weighting == 'tf':
          return self.term_frequency_weight(query)
        elif self.term_weighting == 'tfidf':
          return self.tfidf_weight(query)
          
        #return list(range(1,11))

    # A method to precompute the inverse document frequency value of each term in the
    # collection, again based just on the inverted index. Thus, the index maps each term to
    # the documents that contain it, whose number determines its document frequency.

    def method1(self): 
      pass

    # A method to precompute the document vector size for each document in the collection
    # Note that this can be computed for all documents at the same time, in a single pass over
    # the index. Where TF.IDF term weighting is used, the IDF values must be computed before
    # the document vector sizes are calculated.

    def method2(self): 
      pass


    # A method that calculates weights using the Binary weight scheme ( whether or not a term is present)
    def binary_term_weight(self, query):
      pass

    def term_frequency_weight(self, query):
      pass

    def tfidf_weight(self, query):
      pass

