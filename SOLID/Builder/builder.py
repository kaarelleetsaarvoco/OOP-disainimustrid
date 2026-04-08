class CodeBuilder:
    """Builder class for constructing Python class definitions"""
    
    def __init__(self, class_name):
        """
        Initialize the CodeBuilder with a class name.
        
        Args:
            class_name: The name of the class to build
        """
        self.class_name = class_name
        self.fields = []
    
    def add_field(self, name, value):
        """
        Add a field to the class.
        Supports method chaining by returning self.
        
        Args:
            name: The field name (e.g., 'name')
            value: The default value (e.g., '""' or '0')
            
        Returns:
            self: For method chaining
        """
        self.fields.append((name, value))
        return self
    
    def __str__(self):
        """
        Generate the Python class definition as a string.
        Uses 2 spaces for method indentation and 4 spaces for body.
        
        Returns:
            A string containing the complete class definition
        """
        lines = []
        lines.append(f"class {self.class_name}:")
        lines.append("  def __init__(self):")
        
        for field_name, field_value in self.fields:
            lines.append(f"    self.{field_name} = {field_value}")
        
        return "\n".join(lines)


# Example usage
if __name__ == "__main__":
    cb = (CodeBuilder('Person')
          .add_field('name', '""')
          .add_field('age', '0'))
    
    print(cb)
