
import math

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
      self.get_inverse_document_frequency()
      return list(range(1,11))
        # if self.term_weighting == 'binary':
        #   return self.binary_term_weight(query)
        # elif self.term_weighting == 'tf':
        #   return self.term_frequency_weight(query)
        # elif self.term_weighting == 'tfidf':
        #   return self.tfidf_weight(query)
          
      # return self.get_candidate_document_ids(query)


    # This Function returns the idf (Inverse Document Frequency) value for each term in inverted index

    def get_inverse_document_frequency(self):
      index = self.index
      total_docs = self.num_docs
      document_frequency = dict() # maps a term to integer(document number)
      inverse_document_frequency = dict() # maps a term to inverse document frequency

      # Calculates Document Frequency value for each term
      for term in index:
        df = len(index[term]) # calculates document frequency
        document_frequency.update({ term: df })

      #Calculates Inverse Document Frequency value for each term
      for term in index:
        idf = math.log(total_docs/document_frequency[term], 10)
        inverse_document_frequency.update({ term: idf })

      return inverse_document_frequency

      

    # gets all candidate document ids ( documents with at least one term from the query)
    # def get_candidate_document_ids(self, query):
    #   # print(query)
    #   documents = self.index
    #   candidate_document_ids = []
    #   for query_term in query:
    #     for term in documents:
    #       if query_term == term:
    #         document_ids = list(documents[term].keys())
    #         candidate_document_ids.extend(document_ids)
    #   candidate_document_ids = list(dict.fromkeys(candidate_document_ids)) #removes duplicates
    #   return candidate_document_ids


    def term_frequency_weight(self, query):
      pass

    def tfidf_weight(self, query):
      pass

