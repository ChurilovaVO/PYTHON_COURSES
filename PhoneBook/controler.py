import view
import text_fields as txt
import model


def start_pb():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.load_file()
                view.print_info(txt.load_succeSSful)
            case 2:
                model.save_contact()
                view.print_info(txt.save_successful)
            case 3:
                pb=model.get_pb()
                view.show_contact(pb, txt.no_contact_or_file)
            case 4:
                contact=view.new_contact()
                model.add_contact(contact)
                view.print_info(txt.new_contact_successful)
            case 5:
                find_contact=view.print_contact(txt.find_info)
                result_contact=model.find_contact(find_contact)
                if result_contact:
                    view.show_contact(result_contact, txt.no_contact_or_file)
                else:
                    view.print_info(txt.not_coincidence)
            case 6:
                find_contact_for_change=view.print_contact(txt.find_change_contact)
                result_contact=model.find_contact(find_contact_for_change)
                choice = view.change_menu()
                if choice==1:
                    new_name=view.print_contact(txt.new_name)
                    model.change_contact(result_contact, new_name,choice)
                    view.print_info(txt.new_change_name)
                if choice==2:
                    new_tel=view.print_contact(txt.new_phone)
                    model.change_contact(result_contact, new_tel,choice)
                    view.print_info(txt.new_change_tel)
                if choice==3:
                    new_com=view.print_contact(txt.new_comment)
                    model.change_contact(result_contact, new_com,choice)
                    view.print_info(txt.new_change_com)
            case 7:
                find_contact_for_change=view.print_contact(txt.start_delete_contact)
                result_contact=model.find_contact(find_contact_for_change)
                choice=view.confirm(txt.confirm_delete_contact)
                if choice==True:
                    model.delete_contact(result_contact,choice)
                    view.print_info(txt.result_delete_contact)
                else:
                    view.change_menu()
            case 8:
                if model.exit_pb():
                    if view.confirm(txt.is_changed):
                        model.save_contact()
                view.print_info(txt.bye_bye)
                exit()
         
            