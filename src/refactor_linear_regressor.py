def calculate_coefficients(self):
    coefficients = {}
    pairwise_interactions_dataframe = self.dataframe.filter_columns([column for column in self.dataframe.columns if column != 'ratings'])
    X_matrix = Matrix(elements=pairwise_interactions_dataframe.append_pairwise_interactions().to_array())
    Y_matrix = Matrix(elements=self.dataframe.filter_columns('ratings').to_array())
    result = ((X_matrix.transpose().matrix_multiply(X_matrix)).inverse()).matrix_multiply(X_matrix.transpose()).matrix_multiply(Y_matrix)
    coeff_result = [arr[0] for arr in result.elements]
    for i, key in enumerate(self.dataframe.data_dict.keys()):
        coefficients[key] = coeff_result[i]
    return coefficients
