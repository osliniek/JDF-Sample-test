import xml.etree.ElementTree as ET
import os

def validate_jdf(file_path):
    print(f"Testing JDF file: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        # Strip namespace for easier tag checking in this simple script
        # JDF usually has a namespace like http://www.CIP4.org/JDFSchema_1_1
        
        tag_name = root.tag
        if '}' in tag_name:
            tag_name = tag_name.split('}', 1)[1]
            
        print(f"Root Element: {tag_name}")
        
        if tag_name != 'JDF':
            print("Error: Root element is not 'JDF'")
            return
            
        # Check standard attributes
        jdf_id = root.attrib.get('ID', 'N/A')
        status = root.attrib.get('Status', 'N/A')
        jdf_type = root.attrib.get('Type', 'N/A')
        version = root.attrib.get('Version', 'N/A')
        
        print(f"JDF ID: {jdf_id}")
        print(f"Status: {status}")
        print(f"Type:   {jdf_type}")
        print(f"Version:{version}")
        
        if jdf_id == 'N/A' or status == 'N/A' or jdf_type == 'N/A':
            print("Warning: Missing one or more critical attributes (ID, Status, Type).")
        else:
            print("Success: JDF structure appears valid for a basic check.")

    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    validate_jdf("sample.jdf")
