if __name__ == "__main__":
    input_sap_num: str = "12.334,34"
    print(f"{input_sap_num = }")
    print(f"{input_sap_num.replace('.', ',').replace(',', '.') = }")
    print(f"{input_sap_num.translate(str.maketrans({',': '.', '.': ','})) = }")
