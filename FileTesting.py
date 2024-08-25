def InsertText(file_path, html_content):
    try:
        with open(file_path, 'r+') as file:
            # Read the entire file content
            file_content = file.read()

            # Find a specific marker (you can adjust this marker)
            marker = "<!-- Insert Slip -->"
            start_index = file_content.find(marker)

            # If the marker is found, insert the HTML content
            if start_index != -1:
                file_content = file_content.replace(marker, marker + html_content)

                # Rewrite the file with the updated content
                file.seek(0)
                file.write(file_content)
                file.truncate()

                print("HTML content inserted successfully.")
            else:
                print("Marker '<!-- Insert Slip -->' not found in the file.")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")


# Example usage:
file_path = 'templates/index.html'
html_content = f"""


                    <div class="slip" onclick="openImage(src='Images/Slips.png')">
                        <div class="slip-img">
                            <img src="Images/Slips.png" alt="Slip Image">
                        </div>
                        <div class="slip-info">
                            <h3>SLIP 001</h3>
                            <p>DATE: MAY 2024, ITEMS:
                            MILK, BREAD, CHEESE</p>
                        </div>
                    </div>
"""

InsertText(file_path, html_content)