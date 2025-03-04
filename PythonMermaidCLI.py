# npm install -g @mermaid-js/mermaid-cli

#Save it as `diagram.md` and open in a **Markdown viewer with Mermaid support**.

#---

### **Option 3: Convert Mermaid to PNG using Python**
#If you want to **convert the Mermaid diagram to an image**, use `mermaid-js` or `pymermaid`:

#### **Python Script (Generate PNG)**
#python

# https://mermaid.js.org/ecosystem/integrations-community.html#llm-integrations

import subprocess

# Mermaid diagram code (saved as a file)
mermaid_code = """classDiagram
    class Serializable {
        <<abstract>>
    }
    
    class BaseMessage {
        +content: Union[str, list]
        +additional_kwargs: dict
        +response_metadata: dict
        +type: str
        +name: Optional[str]
        +id: Optional[str]
        +__init__(content, **kwargs)
        +is_lc_serializable() bool
        +get_lc_namespace() list[str]
        +text() str
        +__add__(other) ChatPromptTemplate
        +pretty_repr(html) str
        +pretty_print()
    }
    
    class BaseMessageChunk {
        +get_lc_namespace() list[str]
        +__add__(other) BaseMessageChunk
    }
    
    %% Functions
    class merge_content {
        <<function>>
        +merge_content(first_content, *contents)
    }
    
    class message_to_dict {
        <<function>>
        +message_to_dict(message) dict
    }
    
    class messages_to_dict {
        <<function>>
        +messages_to_dict(messages) list[dict]
    }
    
    class get_msg_title_repr {
        <<function>>
        +get_msg_title_repr(title, bold) str
    }
    
    Serializable <|-- BaseMessage
    BaseMessage <|-- BaseMessageChunk
    BaseMessageChunk ..> merge_content : uses
    BaseMessage ..> get_msg_title_repr : uses
    message_to_dict ..> BaseMessage : takes as input
    messages_to_dict ..> BaseMessage : takes as input
"""

# Save to a file
with open("diagram.mmd", "w") as f:
    f.write(mermaid_code)

# Convert to PNG using Mermaid CLI (install mermaid-js globally with npm)
subprocess.run(["mmdc", "-i", "diagram.mmd", "-o", "diagram.png"])

print("Mermaid diagram saved as diagram.png")
