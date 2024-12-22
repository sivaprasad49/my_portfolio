from sentence_transformers import SentenceTransformer

def create_embeddings(series_to_embed: Union[str, pd.Series], model) -> List:
    embeddings = model.encode(series_to_embed, convert_to_tensor=True).tolist()
    return embeddings


modelPath = f'/Users/My_Drive/my_repository/repository/execgant/execgant/ml_model'
semantic_model = SentenceTransformer(modelPath)


to_embed = "Siva"
embeddings = create_embeddings(series_to_embed=to_embed,
                                               model=semantic_model)


#output=[675.7, 675.3, 98.4]
#output = {name='Siva', "Gender": "Male"}


