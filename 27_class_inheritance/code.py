class Device:
    def __init__(self, name, connected_by) -> None:
        self.name = name
        self.connected_by = connected_by
        self.connected = True
        
    def __str__(self) -> str:
        return f"Device {self.name!r} ({self.connected_by})"
    
    def disconnect(self):
        self.connected = False
        print("Disconnected.")
        
class Printer(Device):
    def __init__(self, name, connected_by, capacity) -> None:
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity
        
    def __str__(self) -> str:
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"
    
    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages
  
printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer = Device("Printer", "USB")
print(printer)
printer.disconnect()