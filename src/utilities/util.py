
def ValidEntry(Model, **kwargs):
    """Check for valid model status. \nModel: Your SQLalchemy model\nparams: Conditions to query by (accepts many)"""
    return Model.query.filter_by(
        **kwargs
    ).first()
