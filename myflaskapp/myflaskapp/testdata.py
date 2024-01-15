import json
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

# JSON Schema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "Prompt Table": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string" },
          "prompt": { "type": "string" },
          "response": { "type": "string" }
        },
        "required": ["id", "prompt", "response"]
      }
    }
  },
  "required": ["Prompt Table"]
}

# JSON Data
json_data = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "Worldbuilding",
    "description": "Worldbuilding is the process of constructing an imaginary world, sometimes associated with a whole fictional universe. The resulting world may be called a constructed world. Developing an imaginary setting with coherent qualities such as a history, geography, and ecology is a key task for many science fiction or fantasy writers.",
    "Master List":{
        "type": "object",
        "properties":{
            "Worldbuilding":{
                        "Plot Elements": [{
                                            "Conflict": [
                                                                {
                                                                    "ID": 1,
                                                                    "Aspect": "Character vs. Character",
                                                                    "Description": "The protagonist faces opposition from another character or characters."
                                                                },
                                                                {
                                                                    "ID": 2,
                                                                    "Aspect": "Character vs. Self",
                                                                    "Description": "The protagonist struggles with internal issues such as fear, guilt, or a moral dilemma."
                                                                },
                                                                {
                                                                    "ID": 3,
                                                                    "Aspect": "Character vs. Society",
                                                                    "Description": "The protagonist is in conflict with societal norms, laws, or expectations."
                                                                },
                                                                {
                                                                    "ID": 4,
                                                                    "Aspect": "Character vs. Nature",
                                                                    "Description": "The protagonist is pitted against natural forces, like a storm, a desert, or a disease."
                                                                },
                                                                {
                                                                    "ID": 5,
                                                                    "Aspect": "Character vs. Supernatural",
                                                                    "Description": "The protagonist encounters supernatural forces or entities."
                                                                }
                                            ],
                                            "Tension": [
                                                {
                                                    "ID": 6,
                                                    "Aspect": "Raising Stakes",
                                                    "Description": "Make the consequences of failure more severe or personal."
                                                },
                                                {
                                                    "ID": 7,
                                                    "Aspect": "Unpredictability",
                                                    "Description": "Introduce unexpected twists or obstacles that complicate the situation."
                                                },
                                                {
                                                    "ID": 8,
                                                    "Aspect": "Pacing",
                                                    "Description": "Use pacing to control the intensity of the story. Slower moments allow for character development, while faster moments ramp up the tension."
                                                },
                                                {
                                                    "ID": 9,
                                                    "Aspect": "Information Control",
                                                    "Description": "Reveal information strategically to keep the audience guessing."
                                                }
                                            ],
                                            "Plot Twists and Turns": [
                                                {
                                                    "ID": 10,
                                                    "Aspect": "Unpredictability",
                                                    "Description": "A good plot twist should be unexpected, providing a surprise to the audience. It should veer away from clich\u00e9s and predictability, keeping the readers or viewers on their toes."
                                                },
                                                {
                                                    "ID": 11,
                                                    "Aspect": "Foreshadowing",
                                                    "Description": "While a twist should be surprising, it should not come out of nowhere. Effective foreshadowing means that in hindsight, the audience can pick up on subtle clues or hints that lead up to the twist, making it seem plausible and well-integrated into the story."
                                                },
                                                {
                                                    "ID": 12,
                                                    "Aspect": "Impact on the Story",
                                                    "Description": "A great plot twist should have a significant impact on the story's direction or the understanding of characters and events. It's not just there for shock value but plays a crucial role in the narrative, often changing the stakes or the goals of the characters."
                                                },
                                                {
                                                    "ID": 13,
                                                    "Aspect": "Consistency and Logic",
                                                    "Description": "The twist should be consistent with the story's established world and characters. It should make sense within the logic of the story's universe, even if it challenges the audience's initial perceptions."
                                                },
                                                {
                                                    "ID": 14,
                                                    "Aspect": "Character Development",
                                                    "Description": "Good twists often lead to character growth or reveal deeper Columns of a character. They can test the characters, push them out of their comfort zones, or force them to confront truths about themselves."
                                                },
                                                {
                                                    "ID": 15,
                                                    "Aspect": "Emotional Response",
                                                    "Description": "A strong plot twist can elicit a powerful emotional response from the audience, whether it's shock, excitement, sadness, or even betrayal. The emotional investment in the twist is what makes it memorable."
                                                },
                                                {
                                                    "ID": 16,
                                                    "Aspect": "Advances the Plot",
                                                    "Description": "The twist should advance the plot or theme in some way, rather than just being a diversion or a dead end. It should propel the story forward and add depth to the narrative."
                                                },
                                                {
                                                    "ID": 17,
                                                    "Aspect": "Re-watchability/Re-readability",
                                                    "Description": "In the case of movies or books, a good plot twist adds a layer of re-watchability or re-readability. When the audience knows the twist, they can enjoy the story from a new perspective and appreciate the craft of how it was built up."
                                                }
                                            ],
                                            "Climax": [
                                                {
                                                    "ID": 18,
                                                    "Aspect": "Showcase the Central Conflict",
                                                    "Description": "It should directly address the central conflict or problem introduced in the story, whether it's a confrontation, a difficult decision, or an internal struggle."
                                                },
                                                {
                                                    "ID": 19,
                                                    "Aspect": "Be the Turning Point",
                                                    "Description": "The climax should be the turning point in the story, after which the main issue starts to resolve. It often results in a change in the protagonist\u2019s situation, understanding, or perspective."
                                                },
                                                {
                                                    "ID": 20,
                                                    "Aspect": "Be Emotionally Charged",
                                                    "Description": "A great climax evokes strong emotions. Whether it's suspense, excitement, fear, or joy, it should make the reader feel deeply invested in the outcome."
                                                },
                                                {
                                                    "ID": 21,
                                                    "Aspect": "Reflect the Story's Themes",
                                                    "Description": "The climax should embody the core themes of the story, bringing them to the forefront in a powerful way."
                                                },
                                                {
                                                    "ID": 22,
                                                    "Aspect": "Show Character Growth",
                                                    "Description": "This is where the character\u2019s growth or change is highlighted. The protagonist might use new skills or understandings gained throughout the story to confront the climax."
                                                }
                                            ],
                                            "Resolution": [
                                                {
                                                    "ID": 23,
                                                    "Aspect": "Resolve Conflicts",
                                                    "Description": "It should address the outcomes of the climax and resolve any remaining conflicts or questions, providing a sense of completion."
                                                },
                                                {
                                                    "ID": 24,
                                                    "Aspect": "Show Consequences",
                                                    "Description": "The resolution depicts the consequences of the climax, showing how the events have affected the characters and the world of the story."
                                                },
                                                {
                                                    "ID": 25,
                                                    "Aspect": "Provide Satisfaction",
                                                    "Description": "It should leave the reader feeling satisfied, even if the ending isn\u2019t traditionally happy. The resolution needs to feel earned and true to the story."
                                                },
                                                {
                                                    "ID": 26,
                                                    "Aspect": "Offer Reflection",
                                                    "Description": "A good resolution often gives characters and readers a chance to reflect on the journey and its impact."
                                                },
                                                {
                                                    "ID": 27,
                                                    "Aspect": "Set the Future Tone",
                                                    "Description": "In some cases, especially in series, the resolution might also set the stage for future stories, hinting at new adventures or challenges."
                                                }
                                            ]}],
                        "Character Development": [{                    
                                            "Backstory and Motivation": [
                                                {
                                                    "ID": 1,
                                                    "Aspect": "Detailed Background",
                                                    "Description": "Dive deeper into a character's past, exploring their upbringing, significant life events, and the cultural or social environment that influenced them."
                                                },
                                                {
                                                    "ID": 2,
                                                    "Aspect": "Personal Drives and Desires",
                                                    "Description": "Clarify what each character wants or strives for, whether it's personal goals, ideals, fears, or ambitions."
                                                },
                                                {
                                                    "ID": 3,
                                                    "Aspect": "Influential Relationships",
                                                    "Description": "Detail important relationships that have shaped the character, such as mentors, rivals, loved ones, or adversaries."
                                                },
                                                {
                                                    "ID": 4,
                                                    "Aspect": "Foundational Experiences",
                                                    "Description": "Discuss key childhood or early life experiences that significantly shaped the character's worldview and personality."
                                                },
                                                {
                                                    "ID": 5,
                                                    "Aspect": "Cultural Influences",
                                                    "Description": "Explore how the character's cultural background and societal norms influence their motivations and actions."
                                                },
                                                {
                                                    "ID": 6,
                                                    "Aspect": "Formative Traumas",
                                                    "Description": "Include impactful traumatic events and how they affect the character's fears, motivations, and behavior."
                                                }
                                            ],
                                            "Character Arcs": [
                                                {
                                                    "ID": 7,
                                                    "Aspect": "Transformation Journey",
                                                    "Description": "Map out the character's journey of change, showing how they evolve in response to story events and challenges."
                                                },
                                                {
                                                    "ID": 8,
                                                    "Aspect": "Milestones of Growth",
                                                    "Description": "Identify key moments or events in the story that act as catalysts for the character's growth or change."
                                                },
                                                {
                                                    "ID": 9,
                                                    "Aspect": "Resolution of Internal Conflicts",
                                                    "Description": "Show how characters resolve their internal struggles and conflicts as part of their arc."
                                                },
                                                {
                                                    "ID": 10,
                                                    "Aspect": "Evolution of Beliefs",
                                                    "Description": "Trace how the character's beliefs and values change throughout the story."
                                                },
                                                {
                                                    "ID": 11,
                                                    "Aspect": "Challenges Overcome",
                                                    "Description": "Describe the difficulties the character faces and how overcoming these challenges contributes to their growth."
                                                },
                                                {
                                                    "ID": 12,
                                                    "Aspect": "Epiphanies and Realizations",
                                                    "Description": "Highlight moments of realization that lead to significant changes in the character's perspective or behavior."
                                                }
                                            ],
                                            "Consistency and Complexity": [
                                                {
                                                    "ID": 13,
                                                    "Aspect": "Behavioral Patterns",
                                                    "Description": "Establish patterns in the character's behavior that align with their personality and history, ensuring they act believably within those parameters."
                                                },
                                                {
                                                    "ID": 14,
                                                    "Aspect": "Multidimensional Traits",
                                                    "Description": "Develop layers to the character, such as conflicting desires, hidden fears, or unexpected strengths, to create depth."
                                                },
                                                {
                                                    "ID": 15,
                                                    "Aspect": "Dynamic Reactions",
                                                    "Description": "Illustrate how the character reacts differently to various situations, showing a range of emotions and responses."
                                                },
                                                {
                                                    "ID": 16,
                                                    "Aspect": "Inconsistent Behaviors",
                                                    "Description": "Acknowledge and explain instances where the character acts out of character, providing depth and complexity."
                                                },
                                                {
                                                    "ID": 17,
                                                    "Aspect": "Internal Conflicts",
                                                    "Description": "Delve into the character's internal battles, such as moral dilemmas or emotional struggles."
                                                },
                                                {
                                                    "ID": 18,
                                                    "Aspect": "Change Over Time",
                                                    "Description": "Show how the character's responses and behaviors evolve over the course of the story."
                                                }
                                            ],
                                            "Relatability": [
                                                {
                                                    "ID": 19,
                                                    "Aspect": "Universal Themes and Emotions",
                                                    "Description": "Incorporate universal themes or emotions in the character's journey, such as love, loss, ambition, or redemption."
                                                },
                                                {
                                                    "ID": 20,
                                                    "Aspect": "Flaws and Vulnerabilities",
                                                    "Description": "Give characters relatable flaws and vulnerabilities, making them more human and approachable."
                                                },
                                                {
                                                    "ID": 21,
                                                    "Aspect": "Aspirational Qualities",
                                                    "Description": "Include aspirational or admirable qualities in characters, allowing readers to look up to them or draw inspiration from them."
                                                },
                                                {
                                                    "ID": 22,
                                                    "Aspect": "Connections to Other Characters",
                                                    "Description": "Detail how relationships with other characters make them more relatable and add depth to their personality."
                                                },
                                                {
                                                    "ID": 23,
                                                    "Aspect": "Realistic Goals and Struggles",
                                                    "Description": "Include realistic and relatable goals, aspirations, and struggles that readers can empathize with."
                                                },
                                                {
                                                    "ID": 24,
                                                    "Aspect": "Humor and Wit",
                                                    "Description": "Integrate moments of humor or wit to make the character more endearing and relatable to the audience."
                                                }
                                            ]}],
                        "Story Elements": [{  
                                            "Strong Character Development": [
                                                {
                                                    "ID": 1,
                                                    "Aspect": "Backstory and Motivation",
                                                    "Description": "Develop each character\u2019s history and what drives them. This includes their past experiences, family dynamics, and formative events that shaped their personality."
                                                },
                                                {
                                                    "ID": 2,
                                                    "Aspect": "Character Arcs",
                                                    "Description": "Plan how characters evolve throughout the story. This could involve overcoming personal flaws, adapting to new situations, or experiencing significant growth or change."
                                                },
                                                {
                                                    "ID": 3,
                                                    "Aspect": "Consistency and Complexity",
                                                    "Description": "Ensure characters are consistent in their actions and reactions, but also complex enough to avoid being predictable or one-dimensional."
                                                },
                                                {
                                                    "ID": 4,
                                                    "Aspect": "Relatability",
                                                    "Description": "Create characters that readers can relate to or empathize with, even if they are set in a fantastical or unfamiliar world."
                                                }
                                            ],
                                            "Vivid World-Building": [
                                                {
                                                    "ID": 5,
                                                    "Aspect": "Sensory Details",
                                                    "Description": "Incorporate sights, sounds, smells, and textures to make the world feel tangible."
                                                },
                                                {
                                                    "ID": 6,
                                                    "Aspect": "Cultural and Social Structure",
                                                    "Description": "Outline the rules, traditions, and social norms of the world. This includes political systems, religious beliefs, and social customs."
                                                },
                                                {
                                                    "ID": 7,
                                                    "Aspect": "Geography and Environment",
                                                    "Description": "Describe the physical landscape and how it affects the story and the characters. This could be a bustling city, a remote village, or an alien planet."
                                                },
                                                {
                                                    "ID": 8,
                                                    "Aspect": "Magic or Technology",
                                                    "Description": "If applicable, define the rules and limitations of magic or technology in the world."
                                                }
                                            ],
                                            "Engaging Plot": [
                                                {
                                                    "ID": 9,
                                                    "Aspect": "Conflict and Tension",
                                                    "Description": "Establish a central conflict and build tension around it. This could be character vs. character, character vs. self, character vs. society, etc."
                                                },
                                                {
                                                    "ID": 10,
                                                    "Aspect": "Plot Twists and Turns",
                                                    "Description": "Introduce unexpected developments that keep the story unpredictable and interesting."
                                                },
                                                {
                                                    "ID": 11,
                                                    "Aspect": "Climax and Resolution",
                                                    "Description": "Build up to a satisfying climax where the main conflict is confronted, followed by a resolution that ties up the story\u2019s loose ends."
                                                }
                                            ],
                                            "Emotional Depth": [
                                                {
                                                    "ID": 12,
                                                    "Aspect": "Internal Conflicts",
                                                    "Description": "Explore the internal struggles and conflicts of characters to create an emotional connection with the reader."
                                                },
                                                {
                                                    "ID": 13,
                                                    "Aspect": "Show, Don\u2019t Tell",
                                                    "Description": "Use actions, reactions, and dialogues to convey emotions rather than simply stating them."
                                                },
                                                {
                                                    "ID": 14,
                                                    "Aspect": "Empathy and Connection",
                                                    "Description": "Create situations and dilemmas that evoke empathy and emotional investment from the reader."
                                                }
                                            ],
                                            "Cultural and Historical Accuracy": [
                                                {
                                                    "ID": 15,
                                                    "Aspect": "Research",
                                                    "Description": "Conduct thorough research to accurately depict the cultures and historical settings you\u2019re writing about."
                                                },
                                                {
                                                    "ID": 16,
                                                    "Aspect": "Sensitivity Reading",
                                                    "Description": "Consider consulting with cultural or historical experts to ensure respectful and accurate representation."
                                                },
                                                {
                                                    "ID": 17,
                                                    "Aspect": "Avoiding Stereotypes",
                                                    "Description": "Be mindful of avoiding stereotypes and presenting nuanced, respectful portrayals."
                                                }
                                            ],
                                            "Innovative Narrative Techniques": [
                                                {
                                                    "ID": 18,
                                                    "Aspect": "Non-Linear Storytelling",
                                                    "Description": "Experiment with telling the story out of chronological order."
                                                },
                                                {
                                                    "ID": 19,
                                                    "Aspect": "Multiple Points of View",
                                                    "Description": "Use different characters\u2019 perspectives to provide a broader understanding of the story."
                                                },
                                                {
                                                    "ID": 20,
                                                    "Aspect": "Unreliable Narrators",
                                                    "Description": "Employ narrators whose credibility is questionable, adding intrigue and complexity."
                                                }
                                            ],
                                            "Appropriate Language and Style": [
                                                {
                                                    "ID": 21,
                                                    "Aspect": "Audience Consideration",
                                                    "Description": "Tailor your language complexity, tone, and style to suit your intended audience."
                                                },
                                                {
                                                    "ID": 22,
                                                    "Aspect": "Consistency in Style",
                                                    "Description": "Maintain a consistent narrative voice and style throughout the story."
                                                },
                                                {
                                                    "ID": 23,
                                                    "Aspect": "Dialogue vs Description",
                                                    "Description": "Balance the use of dialogue and descriptive language to suit the genre and audience preferences."
                                                }
                                            ]}],
                        "World Building Elements": [{ 
                                            "Sensory Details": [
                                                {
                                                    "ID": 1,
                                                    "Aspect": "Visual Details",
                                                    "Description": "Describe what the environment looks like. This can include the colors, shapes, and sizes of objects, the interplay of light and shadow, and the overall scenery. For instance, you might describe the vibrant hues of a bustling market, the stark, imposing architecture of a dystopian city, or the serene beauty of a forest at dawn."
                                                },
                                                {
                                                    "ID": 2,
                                                    "Aspect": "Auditory Details",
                                                    "Description": "Convey what characters hear in the environment. This could be the hustle and bustle of city life, the tranquil sounds of nature, or the eerie silence of an abandoned place. For example, the cacophony of voices and traffic in an urban setting, the chirping of birds and rustling of leaves in a forest, or the haunting echo of footsteps in an empty hall."
                                                },
                                                {
                                                    "ID": 3,
                                                    "Aspect": "Olfactory Details",
                                                    "Description": "Incorporate smells to give a sense of the environment's atmosphere. This might include the aroma of food from a nearby caf\u00e9, the scent of rain on pavement, or the mustiness of an old library. Descriptions of smell can powerfully evoke memories and emotions in readers."
                                                },
                                                {
                                                    "ID": 4,
                                                    "Aspect": "Gustatory Details",
                                                    "Description": "While not always applicable, taste can be used effectively in certain contexts. This could be the taste of salt in the sea air, the flavor of street food, or the bitterness of smoke in a post-apocalyptic landscape."
                                                },
                                                {
                                                    "ID": 5,
                                                    "Aspect": "Tactile Details",
                                                    "Description": "Describe what characters feel physically. This includes textures and temperatures, like the roughness of a stone wall, the chill of a foggy morning, or the oppressive heat of a desert. Physical sensations can make the environment feel tangible."
                                                }
                                            ],
                                            "Defined Social Hierarchy and Classes": [
                                                {
                                                    "ID": 6,
                                                    "Aspect": "Description",
                                                    "Description": "Establish clear social strata, such as nobility, merchants, artisans, and peasants in a historical setting, or different factions, corporations, or guilds in a science fiction or fantasy world."
                                                },
                                                {
                                                    "ID": 7,
                                                    "Aspect": "Interaction",
                                                    "Description": "Show how these classes interact, their roles in society, and the dynamics between them."
                                                }
                                            ],
                                            "Belief Systems and Religions": [
                                                {
                                                    "ID": 8,
                                                    "Aspect": "Creation",
                                                    "Description": "Create belief systems or religions that shape the values, traditions, and rituals of the society."
                                                },
                                                {
                                                    "ID": 9,
                                                    "Aspect": "Influence",
                                                    "Description": "Detail how these beliefs influence daily life, governance, and the world's history."
                                                }
                                            ],
                                            "Political Structure": [
                                                {
                                                    "ID": 10,
                                                    "Aspect": "Government Types",
                                                    "Description": "Define the type of government and political systems in place, whether it's a monarchy, democracy, dictatorship, council, etc."
                                                },
                                                {
                                                    "ID": 11,
                                                    "Aspect": "Leadership and Power",
                                                    "Description": "Include how leaders are chosen, the distribution of power, and the relationship between rulers and the populace."
                                                }
                                            ],
                                            "Laws and Justice System": [
                                                {
                                                    "ID": 12,
                                                    "Aspect": "Legal Framework",
                                                    "Description": "Outline the legal framework governing the society, including laws, regulations, and taboos."
                                                },
                                                {
                                                    "ID": 13,
                                                    "Aspect": "Administration of Justice",
                                                    "Description": "Explain how justice is administered, the role of law enforcement, and the consequences of breaking the law."
                                                }
                                            ],
                                            "Economic Systems": [
                                                {
                                                    "ID": 14,
                                                    "Aspect": "Economic Activities",
                                                    "Description": "Describe the economic activities that sustain the society, such as trade, agriculture, manufacturing, or technology."
                                                },
                                                {
                                                    "ID": 15,
                                                    "Aspect": "Economic Relations",
                                                    "Description": "Include details about currency, trade relations with other societies, and economic challenges."
                                                }
                                            ],
                                            "Cultural Norms and Etiquette": [
                                                {
                                                    "ID": 16,
                                                    "Aspect": "Norms and Customs",
                                                    "Description": "Develop norms, customs, and etiquette that characters in the story adhere to."
                                                },
                                                {
                                                    "ID": 17,
                                                    "Aspect": "Impact on Society",
                                                    "Description": "Show how these norms affect interactions, social status, and relationships."
                                                }
                                            ],
                                            "Traditions and Festivals": [
                                                {
                                                    "ID": 18,
                                                    "Aspect": "Celebrations",
                                                    "Description": "Create festivals, celebrations, and rituals that are significant to the society, reflecting their history, beliefs, and values."
                                                },
                                                {
                                                    "ID": 19,
                                                    "Aspect": "Cultural Showcase",
                                                    "Description": "Use these events to showcase the culture's arts, music, cuisine, and other unique Columns."
                                                }
                                            ],
                                            "Education and Knowledge Dissemination": [
                                                {
                                                    "ID": 20,
                                                    "Aspect": "Knowledge Transfer",
                                                    "Description": "Explain how knowledge is passed down through generations, whether through formal education, apprenticeships, or oral traditions."
                                                },
                                                {
                                                    "ID": 21,
                                                    "Aspect": "Institutions",
                                                    "Description": "Include the role of scholars, libraries, and other institutions in spreading knowledge."
                                                }
                                            ],
                                            "Family Dynamics and Gender Roles": [
                                                {
                                                    "ID": 22,
                                                    "Aspect": "Family Structure",
                                                    "Description": "Portray the structure and role of families, marriage customs, and household dynamics."
                                                },
                                                {
                                                    "ID": 23,
                                                    "Aspect": "Role of Gender",
                                                    "Description": "Define gender roles and expectations, if applicable, and how they influence characters' lives."
                                                }
                                            ],
                                            "Cultural Diversity and Interaction": [
                                                {
                                                    "ID": 24,
                                                    "Aspect": "Multiculturalism",
                                                    "Description": "If the world includes multiple cultures, show how they coexist, interact, and influence each other."
                                                },
                                                {
                                                    "ID": 25,
                                                    "Aspect": "Cultural Dynamics",
                                                    "Description": "Address any conflicts or alliances that arise from cultural differences."
                                                }
                                            ],
                                            "Geography and Environment": [
                                                {
                                                    "ID": 26,
                                                    "Aspect": "Diverse Landscapes",
                                                    "Description": "A richly imagined world should have a variety of geographical features such as mountains, rivers, forests, deserts, oceans, and plains. These landscapes can influence the culture, lifestyle, and behavior of the characters living there."
                                                },
                                                {
                                                    "ID": 27,
                                                    "Aspect": "Climate and Weather Patterns",
                                                    "Description": "The climate of different areas in the world can greatly impact the story. For instance, a harsh, cold climate might shape a community's resilience, while a tropical climate could influence the kind of flora and fauna that exist there."
                                                },
                                                {
                                                    "ID": 28,
                                                    "Aspect": "Natural Resources and Ecosystems",
                                                    "Description": "The availability (or lack) of natural resources like water, minerals, and fertile land can drive conflict and shape societies. The ecosystems should be well thought out, with unique plants and animals that add depth to the world."
                                                },
                                                {
                                                    "ID": 29,
                                                    "Aspect": "Impact on Plot and Characters",
                                                    "Description": "The geography and environment should directly affect the story and its characters. This could mean characters having to navigate difficult terrain, societies formed around particular natural features, or conflicts arising over resources."
                                                },
                                                {
                                                    "ID": 30,
                                                    "Aspect": "Cultural Significance",
                                                    "Description": "Different geographical features might have cultural or spiritual significance for the inhabitants of the world. Sacred mountains, rivers that are lifelines to civilizations, and mysterious forests can all add layers of meaning and history."
                                                },
                                                {
                                                    "ID": 31,
                                                    "Aspect": "Realism and Consistency",
                                                    "Description": "Even in fantastical settings, the geography and environment should follow some internal logic and consistency. For example, a desert next to a rainforest might require an explanation that fits within the story's world."
                                                },
                                                {
                                                    "ID": 32,
                                                    "Aspect": "Sensory Descriptions",
                                                    "Description": "Vivid and detailed descriptions of the environment can enhance the reader's experience. Describing the sights, sounds, smells, and textures of the landscape makes the world more tangible and real."
                                                },
                                                {
                                                    "ID": 33,
                                                    "Aspect": "Interactions with the Environment",
                                                    "Description": "Characters should interact with their environment, whether it's a struggle against harsh weather, navigating tricky landscapes, or using the land's resources for survival or development."
                                                },
                                                {
                                                    "ID": 34,
                                                    "Aspect": "Historical Evolution",
                                                    "Description": "Consider how the geography has shaped the history and development of civilizations within the story. This can include past natural disasters, changes due to human activity, or legendary events tied to specific locations."
                                                },
                                                {
                                                    "ID": 35,
                                                    "Aspect": "Map Creation",
                                                    "Description": "If applicable, creating a map can help both the author and the reader keep track of the geography and understand how it influences the plot and characters."
                                                }
                                            ],
                                            "Magic or Technology Integration with the Environment": [
                                                {
                                                    "ID": 36,
                                                    "Aspect": "Description",
                                                    "Description": "The magic or technology should be deeply interwoven with the world's environment. For instance, if the setting is a lush forest, the magic could involve nature and elements, or if it's a futuristic city, the technology could include advanced urban infrastructure systems."
                                                },
                                                {
                                                    "ID": 37,
                                                    "Aspect": "Influence on Operation",
                                                    "Description": "The environmental features should influence how magic or technology operates. In a desert setting, magic might revolve around controlling sand or water, whereas in a high-tech city, technology could focus on energy efficiency and vertical living spaces."
                                                }
                                            ],
                                            "Magic or Technology Consistency and Rules": [
                                                {
                                                    "ID": 38,
                                                    "Aspect": "Establishment of Rules",
                                                    "Description": "Establish clear rules and limitations for how magic or technology works. This prevents them from becoming a catch-all solution to every problem, thus maintaining tension in the story."
                                                },
                                                {
                                                    "ID": 39,
                                                    "Aspect": "Application Consistency",
                                                    "Description": "Consistency in its application ensures that the reader can understand and anticipate its uses and limitations, which can be critical for plot development and conflict resolution."
                                                }
                                            ],
                                            "Magic or Technology Cultural Influence": [
                                                {
                                                    "ID": 40,
                                                    "Aspect": "Integration in Culture",
                                                    "Description": "Magic or technology should be a part of the cultural fabric. It could shape social structures, religious beliefs, and daily life. For example, a society with healing magic might view healthcare differently."
                                                },
                                                {
                                                    "ID": 41,
                                                    "Aspect": "Social Dynamics",
                                                    "Description": "The development and control of magic or technology can create social hierarchies, conflicts, and power dynamics, adding depth to the narrative."
                                                }
                                            ],
                                            "Magic or Technology Historical Development": [
                                                {
                                                    "ID": 42,
                                                    "Aspect": "Evolution Over Time",
                                                    "Description": "Consider how magic or technology has evolved over time in your world. Its history can add depth and realism, showing how it has shaped society and been shaped by it."
                                                },
                                                {
                                                    "ID": 43,
                                                    "Aspect": "Historical Events",
                                                    "Description": "Historical events, such as magical disasters or technological breakthroughs, can be significant plot points or backstories that enrich the narrative."
                                                }
                                            ],
                                            "Magic or Technology Impact on Characters": [
                                                {
                                                    "ID": 44,
                                                    "Aspect": "Effect on Lives",
                                                    "Description": "The magic or technology should directly affect the characters' lives. It can define their professions, hobbies, and daily routines."
                                                },
                                                {
                                                    "ID": 45,
                                                    "Aspect": "Access and Ability",
                                                    "Description": "Characters might have varying degrees of access or ability, influencing their status and relationships with others."
                                                }
                                            ],
                                            "Magic or Technology Visual and Sensory Descriptions": [
                                                {
                                                    "ID": 46,
                                                    "Aspect": "Sensory Imagery",
                                                    "Description": "Describe how magic or technology looks, feels, sounds, and even smells. Vivid sensory details help to create a more immersive and believable world."
                                                },
                                                {
                                                    "ID": 47,
                                                    "Aspect": "Mood and Tone",
                                                    "Description": "These descriptions can also reflect the mood and tone of different scenes \u2013 for instance, the eerie glow of a spell or the sleek feel of a technological gadget."
                                                }
                                            ],
                                            "Magic or Technology Originality and Creativity": [
                                                {
                                                    "ID": 48,
                                                    "Aspect": "Unique Elements",
                                                    "Description": "While it's fine to draw inspiration from existing works, strive for original elements that set your world apart. This could be a unique source of magic or an innovative technological concept."
                                                },
                                                {
                                                    "ID": 49,
                                                    "Aspect": "Expanding Traditional Tropes",
                                                    "Description": "Think about how you can subvert or expand upon traditional tropes to surprise and engage your readers."
                                                }
                                            ]}]
            }
        }
    }
}                                          
                                

# Validate JSON
try:
    validate(instance=json_data, schema=schema)
    print("JSON data is valid.")
except ValidationError as e:
    print("JSON data is invalid:", e)




def read_json(file_path):
    """ Read data from a JSON file and return it. """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json(file_path, data):
    """ Write data to a JSON file. """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

"""
    # Usage example:

    # Path to the JSON file
    json_file_path = 'path_to_your_json_file.json'

    # Reading the JSON file
    data = read_json(json_file_path)
    print("Data read from JSON:", data)

    # Modifying the data (for example, adding a new prompt-response pair)
    new_entry = {
        "id": "3",
        "prompt": "What is the chemical symbol for water?",
        "response": "H2O"
    }
    data["Prompt Table"].append(new_entry)

    # Writing the modified data back to the JSON file
    write_json(json_file_path, data)
"""