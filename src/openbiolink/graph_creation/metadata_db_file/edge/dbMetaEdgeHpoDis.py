from openbiolink.graph_creation.metadata_db_file.edge.dbMetadataEdge import DbMetadataEdge
from openbiolink.graph_creation.types.dbType import DbType


class DbMetaEdgeHpoDis(DbMetadataEdge):
    NAME = "Edge - HPO - Disease Phenotype"
    # URL = "http://compbio.charite.de/jenkins/job/hpo.annotations/1269/artifact/misc/phenotype_annotation_hpoteam.tab"
    URL = "http://purl.obolibrary.org/obo/hp/hpoa/phenotype_annotation.tab"
    OFILE_NAME = "HPO_disease_phenotype.tab"
    #disease-db	disease-identifier	disease-name	negation	HPO-ID	reference	evidence-code	onset	frequencyHPO	modifier	sub-ontology	alt-names	curators	frequencyRaw	sex

    COLS = [
        "DB", # disease-db	
        "DOI", # disease-identifier	
        "DBname", # disease-name	
        "negation", # negation
        "HPO_ID", # HPO-ID	
        "DB_ref",  # reference	
        "evidence_code", # evidence-code	
        "onsetMod", # onset
        "freq", # frequencyHPO
        "mod", # modifier	
        "sub_ontology", # sub-ontology	
        "alt_names", # alt-names	
        "assigned_by", # curators	
        "freq_raw", # frequencyRaw	
        "sex", # sex
    ]
    FILTER_COLS = ["DB", "DOI", "HPO_ID", "evidence_code"]
    HEADER = 1
    DB_TYPE = DbType.DB_EDGE_HPO_DIS

    def __init__(self):
        super().__init__(
            url=DbMetaEdgeHpoDis.URL, ofile_name=DbMetaEdgeHpoDis.OFILE_NAME, dbType=DbMetaEdgeHpoDis.DB_TYPE
        )
