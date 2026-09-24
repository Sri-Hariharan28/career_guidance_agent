def cutoff_cali(mat,phy,che) -> float:
    """ You are a fnn tool to calculate cutoff for the user
        You will get 3 int as input mat,phy amd che
        You need to calculate the cf
        cf=mat+(phy/2)+(che/2)
        and return cf as a float
    """
    cf=mat+(phy/2)+(che/2)
    return cf