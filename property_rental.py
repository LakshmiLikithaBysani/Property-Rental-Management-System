print("🏠 Property Rental Management System")

properties = []

while True:
    print("\n1. Add Property")
    print("2. View Properties")
    print("3. Search Property")
    print("4. Update Rental Status")
    print("5. Delete Property")
    print("6. Count Properties")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add Property
    if choice == "1":
        property_id = input("Enter property ID: ")
        owner = input("Enter owner name: ")
        property_type = input("Enter property type: ")
        rent = input("Enter monthly rent: ")

        property_details = {
            "id": property_id,
            "owner": owner,
            "type": property_type,
            "rent": rent,
            "status": "Available"
        }

        properties.append(property_details)

        print("✅ Property added successfully!")

    # View Properties
    elif choice == "2":
        if len(properties) == 0:
            print("❌ No properties found.")
        else:
            print("\n🏠 Property Details")
            print("--------------------------")

            for property_details in properties:
                print("Property ID:", property_details["id"])
                print("Owner:", property_details["owner"])
                print("Property Type:", property_details["type"])
                print("Monthly Rent:", property_details["rent"])
                print("Status:", property_details["status"])
                print("--------------------------")

    # Search Property
    elif choice == "3":
        search_id = input("Enter property ID to search: ")

        found = False

        for property_details in properties:
            if property_details["id"] == search_id:
                print("\n✅ Property Found")
                print("Property ID:", property_details["id"])
                print("Owner:", property_details["owner"])
                print("Property Type:", property_details["type"])
                print("Monthly Rent:", property_details["rent"])
                print("Status:", property_details["status"])

                found = True
                break

        if not found:
            print("❌ Property not found.")

    # Update Rental Status
    elif choice == "4":
        update_id = input("Enter property ID: ")

        found = False

        for property_details in properties:
            if property_details["id"] == update_id:

                print("\n1. Available")
                print("2. Rented")

                status_choice = input("Choose rental status: ")

                if status_choice == "1":
                    property_details["status"] = "Available"
                elif status_choice == "2":
                    property_details["status"] = "Rented"
                else:
                    print("❌ Invalid status!")
                    break

                print("✅ Rental status updated successfully!")
                found = True
                break

        if not found:
            print("❌ Property not found.")

    # Delete Property
    elif choice == "5":
        delete_id = input("Enter property ID to delete: ")

        found = False

        for property_details in properties:
            if property_details["id"] == delete_id:
                properties.remove(property_details)

                print("✅ Property deleted successfully!")
                found = True
                break

        if not found:
            print("❌ Property not found.")

    # Count Properties
    elif choice == "6":
        print("🏠 Total Properties:", len(properties))

    # Exit
    elif choice == "7":
        print("Thank you for using Property Rental Management System! 🏠")
        break

    else:
        print("❌ Invalid choice!")
