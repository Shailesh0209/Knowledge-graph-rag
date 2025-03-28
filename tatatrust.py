##############################################################
#-----------Tata-trustSPECIFICATIONS FOR 
            # BUILT HERITAGE CONSERVATION
            # 2021
            # TATA TRUSTS
##############################################################
# 2. Create the Book node and link it to the Topic

def create_book(kg, topic_id):
    # topic_id = kg.create_topic("BRICKS")
    
    book_id = kg.create_book(
        "Tata Trust Specifications for Built Heritage Conservation",
        """FOREWORD
            The Tata Trusts, having worked for decades on preserving monuments in public spaces, initiated an exercise 
            to prepare this document whose urgency lay in the lack of a Specifications Manual and Rates specific 
            for conservation works in built heritage. In a country blessed with a built heritage that spans both time and 
            styles of architecture, conserving this built environment is paramount: it defines the diversity that makes 
            India, the differences that influence and enrich our culture and an understanding of how we live together.
            Conservation  of  monuments  in  public  spaces  revitalises  communities  and  usage  of  the  commons.  
            Conservation  of  heritage  buildings  and  their  continued  or  adaptive  re-use  is  as  vital  in  preserving  an  
            architectural style as it is in preserving environmental costs; and as climate change endangers buildings 
            further, strengthening our built heritage to withstand these increased threats is becoming urgent.
            While  the  Central  Public  Works  Department  (CPWD)  publishes  a  specifications  manual,  with  regular  
            updates, related to modern construction works, the field of built heritage conservation does not have any 
            benchmarked specifications or rates to serve as a guide for undertaking projects.
            As  projects  in  built  heritage  are  on  the  increase  around  the  country,  the  Trusts  commissioned  experts  
            from the sector in partnership with the Aga Khan Trust for Culture, to prepare this document, that collates 
            specifications of materials commonly used in conservation projects and lays down procedures for their 
            correct usage keeping in mind traditional building materials, along with an analysis of rates. The manual 
            focusses on materials such as Lime, Stone, Brick, Timber etc. and processes such as Flooring, Roofing and 
            Landscaping.
            The first of its kind in the field, we hope that this document will support future conservation projects and 
            enable  decision  makers  –  officials,  donors,  corporates,  contractors,  as  well  as  younger  conservation  
            architects entering the field, and government agencies embarking on projects – and serve as the starting 
            point for establishing standards in built heritage conservation. India is a land with two millennia worth 
            of processes and materials, and we hope the document will grow in the future with contributions from 
            practitioners in the conservation of built heritage.
            Ratan N. Tata
            Chairman, Tata Trusts
            TATA TRUSTS
            """
    )
    kg.create_relationship(topic_id, "HAS_BOOK", book_id)

    # 3. Create a Chapter node for "BRICK WORK (FIRED) 
    chapter_id = kg.create_chapter(
        "2. BRICK WORK (FIRED)",
        """This  chapter  provides  information  and  guidance  on  conservation  treatments  for  brickwork  in  heritage  
            structures. The conservation treatments should be carried out in consultation with a conservation architect 
            and engineer-in-charge as per the requirement. This chapter will only apply to fired or baked bricks. 
            Chapter 4, Earth/Mud Work should be referred to for unfired mud bricks/Adobe. """
    )
    kg.create_relationship(book_id, "HAS_CHAPTER", chapter_id)

    # 4. Create a Section node for "2.1 MATERIALS"
    section_id = kg.create_section(
        "2.1 MATERIALS",
        "Materials used for conservation of brick work are given below."
    )
    kg.create_relationship(chapter_id, "HAS_SECTION", section_id)

    # 5. Create a Subsection node for "2.1.1 Water
    #    and link it to the Section node
    subsection_id = kg.create_subsection(
        "2.1.1 Water",
        """Water should be clean and free from contaminants such as oil, acids, alkalis, salts, sugar and vegetable growth. It 
            should meet the latest standards IS: 10500- 2012 for Drinking Water. Only potable water should be used.  Sea water 
            or tidal estuary or brackish water should not be used for any conservation works."""
    )
    kg.create_relationship(section_id, "HAS_SUBSECTION", subsection_id)

    # 6. Create a Subsection node for "2.1.2 Mortar
    #    and link it to the Section node
    subsection_id = kg.create_subsection(
        "2.1.2 Mortar",
        """The mortar for the brick work should be as specified and conform to accepted standards. The proportions of the mortar 
            to be used in conservation will be based on site requirements and established from samples at site. Mortar should also 
            be matched as closely as possible in colour and texture with the existing through a mortar analysis and other relevant 
            tests.  If unable to find an existing sample, then mortar specified should follow the guidelines mentioned in in chapter 
            1, Lime Work or chapter 4, Earth/Mud Work or as specified based on particular site requirements. It should generally 
            be ensured that the mortar for the repair is of the same strength or weaker than the existing brick"""
    )
    kg.create_relationship(section_id, "HAS_SUBSECTION", subsection_id)

    # 7. Create a Subsection node for "2.1.3 Brick
    #    and link it to the Section node
    subsection_id = kg.create_subsection(
        "2.1.3 Brick",
        ("""Bricks for repair and replacement 
            • For conservation of brickwork, replacement bricks should be procured or fabricated to match the characteristics 
            of  existing  bricks  as  closely  as  possible.  Bricks  used  in  heritage  structures  don’t  have  fixed  or  standard  sizes  
            so  it  may  be  necessary  to  have  replacements  specifically  manufactured  for  the  work.  This  should  be  applied  
            especially when special shapes are required. 
            • It is also possible to modify, cut and shape the bricks to match the existing.  However, cutting will increase the 
            surface area of the brick exposed to weathering, and is generally not preferred for exposed brickwork.
            • New bricks should match the dimensions, size, shape, texture and colour range of existing bricks. The new bricks 
            produced after matching the existing should be approved by the conservation architect or engineer-in-charge. 
            New bricks for conservation should conform to IS: 1077- 1992, hand-moulded or as specified and should be 
            made from suitable soils. They should be free from cracks and flaws and nodules of free lime. 
            • If it is possible to secure salvaged bricks, the same should be used in conservation work subject to the approval 
            of the conservation architect. Salvaged brick should be sound, free from chips and gouges on exposed faces. 
            Color  range  and  fabrication  markings  should  match  with  those  of  the  adjacent  bricks.  Remove  mortar  from  all  
            faces of salvaged bricks to ensure full contact with new mortar.  They should be free from fungus, have no deep 
            or  extensive  cracks,  damaged  corners  or  arises,  and  are  free  from  old  mortar.  Any  replacement  bricks  should  
            not exceed approved variations in colour, texture and other characteristics of approved samples. Pick the best 
            possible sample of the original for matching.
            i. Lakhori
            Historically,  baked  bricks  have  been  used  since  ancient  times  with  varying  shapes  sizes  and  technology  for  
            manufacturing,  elaborately  documented  in  historical  texts  and  archaeological  sites.  During  medieval  times  baked  
            bricks or lakhori bricks have been used for construction. These are flat thin red coloured burnt clay bricks without frogs 
            that became increasingly popular element of Mughal architecture but were developed during the Ghurian (12-13 C) 
            period to construct structures with typical elements such as domes, arches, mouldings, cornices, cladding and facing 
            etc. It was easy to create intricate patterns due to the small thickness of Lakhori bricks. Since these were made with 
            hand for specific sites, no standard sizes are documented, though a broad range of sizes are seen. The composition 
            also  varies  regionally  as  also  the  size.  Some  other  regional  names  include  nanakshahi  in  Punjab  and  badshahi  in  
            Kashmir.
            Figure 2.1: Brick sizes as documented in Punjab and Haryana 
            190x100x35, 130x75x35, 130x85x25, 150x95x25   
            Source : INTACH Directory of Traditional Building Crafts of India: Volume 2 Building with Bricks Punjab & Haryana, 2020
            Lakhori bricks fall in this range but exceptions are also found pan India.
            Type 1: (150-200) X (90-120) X (25-40)
            Type 2: (100-140) X (110) X (25-30) 
            ii. Gauged and Moulded Bricks
            Use  of  special  bricks  is  seen  in  cornices,  projecting  courses,  moulded  elements  and  decorative  features.  Some  of  
            these were moulded or and cut or chiseled prior to firing to fit the design requirements. For conservation works, where 
            necessary, these can be obtained by special orders with specific shapes, sizes and designs. When it is not possible 
            to procure special sizes or for smaller repairs, these can be obtained by shaping available bricks to the required sizes. 
            However, this is not recommended for exposed brick masonry. If this is to be done for exposed masonry, care should 
            be taken that the cut surfaces are not exposed to weathering and embedded into the masonry
            Figure 2.2 : Moulded bricks as documented in Punjab and Haryana.
            Source : INTACH Directory of Traditional Building Crafts of India: Volume 2 Building with Bricks Punjab & Haryana, 2020
            iii. Tile Bricks
            Brick tiles are often used in conservation of historic brickwork as replacement of Lakhori bricks are not available. Tile 
            bricks, newer or historic, generally conform to a thickness of 1 1/2 -2” or 4-5 cm, are moulded without frogs and are 
            very similar to Lakhori bricks.
            iv. Brick Bats
            During repairs when required, brick bats should be obtained from well burnt bricks.  Any portion of a brick, cut or 
            broken across its length usually known according to its fraction from the whole size, for example, ½ bats, ¾ bats, etc.  
            v. Common Burnt Clay Bricks 
            These should conform to IS: 1077- 1992 and should be hand moulded. They should be free from nodules of free lime, 
            visible cracks, flaws, warpage and organic matter. Newer bricks may have a frog 100 mm in length 40 mm in width 
            and 10 mm to 20 mm deep on one of its flat sides. Historic bricks retrieved from older structures may be used without 
            frogs.""")
    )
    kg.create_relationship(section_id, "HAS_SUBSECTION", subsection_id)

    # create a subsubsection for 2.1.3.1 Occurrence of Brick
    subsubsection_id = kg.create_subsubsection(
        "2.1.3.1 Occurrence of Brick",
        """Bricks have been a popular construction material across the areas with good soil especially alluvial and black soil. 
            Bricks  are  also  a  typical  characteristic  of  areas  with  lack  of  stone  for  construction.  Areas  with  brick  manufacturing  
            and construction include but are not limited to Kashmir, Punjab, Haryana, Delhi, Uttar Pradesh and Madhya Pradesh, 
            Maharashtra, West Bengal and Bihar."""
    )
    kg.create_relationship(subsection_id, "HAS_SUBSUBSECTION", subsubsection_id)

    # create a subsubsection for 2.1.3.2 Precaution and Care 
    subsubsection_id = kg.create_subsubsection(
        "2.1.3.2 Precaution and Care ",
        """Precautions  and  care  while  handling  brick  should  be  as  specified  section  6,  Precautions  and  Care  in  chapter  1,  
            Introduction """)
    kg.create_relationship(subsection_id, "HAS_SUBSUBSECTION", subsubsection_id)

    # create a subsubsection for2.1.3.3 Delivery, Storage, and Handling 
    subsubsection_id = kg.create_subsubsection(
        "2.1.3.3 Delivery, Storage, and Handling ",
        """Proper packaging, delivery, handling and storage of brick helps to prevent breakage, cracking, chipping, spalling 
            and other damages. 
            a. Bricks should be stored on a firm dry, flat surface and should avoid direct contact with the ground should be 
            avoided.. 
            b. Bricks  should  be  placed  in  a  manner  that  facilitates  easy  handling  and  allows  adequate  air  circulation  
            around the bricks. 
            c. Bricks should be loaded or unloaded with care, and should not be thrown or dumped. 
            d. Bricks should be stacked in regular tiers even as they are unloaded, to minimize breakages and defacement 
            of bricks. 
            e. Bricks of different types and selected for different purposes should be stacked separately.  
            f. Blocks should be placed close to the site of work so that least effort is required for their transportation. 
            g. Bricks should be carried from the stack to the site of placement in small batches as and when necessary. 
            Figure 2.3: Brick Roof
            BrickBrick Work (Fired)
            Fig 2.4: Soil types and brick occurrence in India
            Source: Modified from soil and land use survey map of India
            """
    )
    kg.create_relationship(subsection_id, "HAS_SUBSUBSECTION", subsubsection_id)

    # create a section 2.2. USE OF BRICK IN HERITAGE STRUCTURES
    section_id = kg.create_section(
        "2.2 USE OF BRICK IN HERITAGE STRUCTURES",
        """Walls Exposed
            Walls Plastered
            Arches
            Domes
            Floors and Steps
            Decorative Elements
            """ 
    )
    kg.create_relationship(chapter_id, "HAS_SECTION", section_id)

    # create a section 2.3. DEFECTS
    section_id = kg.create_section(
        "2.3 DEFECTS",
        """Table 2.1: Uses of Brick in Heritage Structures
            2.3. DEFECTS 
            Brick masonry may have many issues due to reasons like weathering and decay, material aging clubbed with lack 
            of  maintenance,  environmental  factors  (including  pollutants),  water  penetration,  structural  faults,  defects  in  original  
            construction, manufacturing defects, vegetation, particularly micro bio growth, etc. The defects should be assessed 
            and diagnosed before applying corrective measures. Most typical issues with bricks are listed below but the list is 
            not exhaustive. For each site the conservation architect and engineer-in-charge should prepare their own list/record 
            of defects using the table below as a baseline, assess them and formulate the conservation treatments accordingly.
            Minor Cracks Refer 2.5.1 Minor Crack and 
            Surface Repairs
            Spalling Refer 2.5.1 Minor Crack and 
            Surface Repairs
            Loose Brickwork Refer 2.5.2 Resetting
            DESCRIPTION            PHOTOGRAPHS            CONSERVATION

            Deteriorated Pointing or Open Joints        Refer 2.5.3 Repointing

            Loose Masonry Cavity                         Refer 2.5.4 Grouting

            Cracks through Brick Masonry               Refer 2.5.5 Stitching

            Deteriorated Brickwork                        Refer 2.5.6 Restoration of Brickwork
            
            Decorative Elements                      Refer 2.5.8 Restoration of Decorative Elements 
            
            """
    )
    kg.create_relationship(chapter_id, "HAS_SECTION", section_id)

    # create a section 2.4. TESTS
    section_id = kg.create_section(
        "2.4 TESTS",
        """
            - In order to correctly match the properties of existing bricks to the new bricks, tests should be performed. These 
            include matching visual, physical, and chemical properties to find properties that are compatible for conservation works.

            - Tests also aid in ascertaining the issue with the existing bricks and brickwork and should be used to make 
            informed assessments and to ensure an appropriate repair.

            - These tests should be done under the guidance of a conservation architect or engineer-in-charge and should 
            be conducted either in the field or in a laboratory.

            - The tests should be performed using current IS Codes provided by the Bureau of Indian Standards.

            - If the tests are not available in the IS Codes, then international standards could be followed, guided by the 
            conservation architect or engineer-in-charge.
            
            REFERENCES FOR TESTS
                - ASTM International (American Society for Testing and Materials)
                - ICCROM ARC: A Laboratory Manual for Architectural Conservators Methods
                - Built Heritage Evaluation - Manual Using Simple Test Conservation of Historic Stone Buildings and Monuments
            """
    )
    kg.create_relationship(chapter_id, "HAS_SECTION", section_id)

    # create a section 2.5. CONSERVATION 
    section_id = kg.create_section(
        "2.5 CONSERVATION",
        """
            Conservation treatments to brickwork should be selected after correcting the underlying causes. This section presents 
            treatments techniques for conservation and should be modified for individual site requirements.
            """
    )
    kg.create_relationship(chapter_id, "HAS_SECTION", section_id)

    # create a subsection 2.5.1 Minor Crack and Surface Repairs
    subsection_id = kg.create_subsection(
        "2.5.1 Minor Crack and Surface Repairs",
        """
            The surface treatments should be carried out after finding out the reason for surface deterioration and correcting it. 
            Surface treatments of brickwork may involve patching with matching material or replacing the surface using brick slips.  
            The choice of treatments method will often depend on the severity, location and the ease with which cutting out may 
            be achieved."""
    )
    kg.create_relationship(section_id, "HAS_SUBSECTION", subsection_id)

    # 2.5.1.1 Brick Patching or Plastic Repair
    subsubsection_id = kg.create_subsubsection(
        "2.5.1.1 Brick Patching or Plastic Repair",
        """The  use  of  plastic  or  mortar  repairs  is  often  used  to  treat  damaged/deteriorated  or  spalled  surfaces  of  one  word  
                brickwork. These repairs are justified where only small amount of work is needed.  In this method, deteriorated brickwork 
                is patched with matching mortar and surrounding joints pointed to achieve the appearance of good brickwork. Patch 
                repairs should be of good quality and workmanship and should not disfigure or change the appearance of the bricks. 
                Patching mortar should be compatible to the existing composition of brickwork. Pigments should be avoided and use 
                of brick dust to match the colour is encouraged.  Conservation architect or engineer-in-charge to note if additional 
                ties or reinforcements are to be inserted to strengthen the patched brickwork and it is securely integrated. If the area 
                to be patched exceeds 50% of the exposed face, the entire brick should be removed and replaced.


                a. Removal of deteriorated brickwork: Remove deteriorated or spalling brick surface, dirt and debris from the 
                area to be repaired. Remove only enough material to allow a minimum patch depth of 15 mm or 25 mm.

                b. Cutting: Undercut the edges of the area to be patched slightly to improve bonding.

                c. Cleaning: Thoroughly clean the area with a bristle brush and water prior to placing patching material.

                d. Patching material: Prepare samples of patching material to match the brick colours and texture to be judged 
                on its wet and dry appearance.

                e. Installing: Place patching material or mortar firmly compacted in layers not exceeding 9 mm thick. Allow 
                each layer to dry out before rewetting and placing the next. When the final layer of patching material is 
                thumbprint hard, it should be tooled to match existing surface texture and profile with special attention to the 
                edges. Do not featheredge patching material.

                f. Cleaning: The surrounding brick masonry should be cleaned of mortar or other spots after the patch is 
                provided.

                g. Pointing: If the patch is next to a joint, then follow joints or surface finishing in the original work, and then 
                repoint it, pointing of adjacent joints should be carried out as a separate operation. Care should be taken to 
                not smear the mortar on good brickwork.

                h. Protecting and curing: Protect repairs against adverse weather conditions of rain and direct sunlight and cure 
                by keeping it moist with dampened jute/hessian by sprinkling of water for a fortnight to ensure slow drying."""
    )
    kg.create_relationship(subsection_id, "HAS_SUBSUBSECTION", subsubsection_id)

    #2.5.1.2 Brick Slips
    subsubsection_id = kg.create_subsubsection(
        "2.5.1.2 Brick Slips",
        """
            In  some  situations,  where  it  is  not  possible  to  remove  the  entire  brick,  it  may  be  useful  to  treatment  small  areas  of  
            brickwork using brick slips. Brick slips are facings of about 25mm (1 inch) thickness although it may be possible to cut 
            thinner slips from whole bricks. Brick slips should match the existing bricks. Repair using brick slips should be limited to 
            individual bricks or to relatively small areas of brickwork. Another alternative could also be used with thin brick tiles. 
            Conservation architect and engineer-in-charge to note if additional pins or reinforcements are to be inserted to ensure 
            that the slips are secured well.
            The brick slip should be applied to clean, even and pre-wetted brick surface of the damaged brickwork with matching 
            mortar compatible with adjacent details and profile.
            a. Cutting: Carefully cut out the deteriorated bricks to a regular shape to receive brick slips without disturbing 
            the adjacent bricks.
            b. Cleaning:  Clean  the  surrounding  cavity  of  loose  mortar  and  other  debris  by  hand  tools  such  as  scalpel/
            hacksaw blade/pointed tools and stiff bristle brushes. Avoid using a flat chisel and hammer to prevent any 
            damage to the existing masonry.

            c. Brick Slips: Prepare or procure brick slips to match the surrounding brick work in colour and texture as much 
            as possible.
            d. Prewetting: Spray the Brick surface to receive slips with water before applying the mortar. 
            e. Installation:  Bed  the  slips  firmly  in  the  prepared  area  on  a  bed  of  lime  mortar  compatible  with  that  in  the  
            original brickwork. 
            f. Cleaning: The areas should be cleaned after the installation of brick slip.
            g. Supporting: The bricks may be temporarily supported if required and specified"""
    )
    kg.create_relationship(subsection_id, "HAS_SUBSUBSECTION", subsubsection_id)

    #  create a subsection 2.5.2 Resetting
    subsection_id = kg.create_subsection(
        "2.5.2 Resetting",
        """
            Sections  of  brickwork  should  be  reset  if  they  become  loose  or  dislodged  whenever  possible  as  directed  by  the  
            conservation architect and the engineer-in-charge. If it is not possible to remove and reinstall then other methods may 
            be specified. 
            a. Cleaning  surrounding  joints:  Clear  out  mortar  joints  around  
            the loose brickwork and carefully remove dislodged bricks.  
            b. Providing  support:  Support  adjacent  brickwork  using  timber  
            shims etc. or some other support mechanism where required. 
            c. Cleaning: Clear all the mortar and debris from where the bricks 
            have been removed. Then clean the bricks of dirt, mortar, and 
            loose debris and retain it for re-use if in sound condition. 
            d. Bricks: Retain all the bricks after removal and cleaning. If some 
            bricks  are  damaged,  they  should  be  replaced  to  match  the  
            existing as specified in section 2.1.3.
            e. Wetting: Pre-wet the surrounding brickwork.
            f. Resetting:  Lay  new  bedding  mortar  as  specified  and  re-set  
            bricks  to  match  the  joint  lines  in  courses,  aligning  with  plumb  
            and  level  of  adjacent  existing  work.    Adjust  bricks  wherever  
            needed to its final position while mortar is soft and plastic.
            g. Cleaning: Clean surrounding areas after the bricks are set.  
            h. Curing: Keep repair work damp till it is cured (48 hours plus)."""
    )   
    kg.create_relationship(section_id, "HAS_SUBSECTION", subsection_id)

    # create a subsection 2.5.3 Repointing
    subsection_id = kg.create_subsection(
        "2.5.3 Repointing",
        """
        • For brick masonry repointing refer section 1.5.4, chapter 1, Lime Work.  
        • Mortar in the joints weather and decay and the open joints can let the water into the building and hence it 
        becomes necessary to replace the mortar (repoint).   
        • Appropriate and matching mortar should be used to repoint. Formulation of repair mortar can be made by 
        testing the original/existing mortar in the brickwork. 
        • The type of pointing should match the existing or as specified by the conservation architect"""
    )
    kg.create_relationship(section_id, "HAS_SUBSECTION", subsection_id)

    # create a subsection 2.5.4 Grouting
    subsection_id = kg.create_subsection(
        "2.5.4 Grouting",
        """
        • Grouting  can  be  used  for  deteriorated  and  loose  brickwork  without  dismantling  and  for  areas  that  are  
            inaccessible from the exterior.  
        • For grouting process, refer section section 1.5.5, chapter 1, Lime Work."""
    )
    kg.create_relationship(section_id, "HAS_SUBSECTION", subsection_id)

    # create a subsection 2.5.5 Stitching
    subsection_id = kg.create_subsection(
        "2.5.5 Stitching",
        """
            Stitching is often used to repair structural cracks when recommended by the conservation architect and engineer-in-
            charge. For stitching process refer section 3.5.8, chapter 3, Stone Work."""
    )
    kg.create_relationship(section_id, "HAS_SUBSECTION", subsection_id)

    # create a subsection 2.5.6 Restoration of Brickwork
    subsection_id = kg.create_subsection(
        "2.5.6 Restoration of Brickwork",
        """
            Brick  work  should  be  replaced  only  when  deteriorated  beyond  repair  and  no  other  repair  method  is  found  to  be  
            suitable. This should be decided after a full evaluation of the building and the damage accurately. Replacement bricks 
            should match the size, colour and texture as per the original. The bonding in the replacement brick should match with 
            existing work"""
    )         
    kg.create_relationship(section_id, "HAS_SUBSECTION", subsection_id)

    # 2.5.6.1  Replacing Small Sections 
    subsubsection_id = kg.create_subsubsection(
        "2.5.6.1 Replacing Small Sections",
        """
        When only two or three bricks are damaged or the damaged areas is less 1 sqm, it will be suitable and cheaper to 
        replace the bricks than to rebuild the entire wall surface/column or any other element. Replacements should be either 
        new matching brick or matching salvaged brick placed so as to replicate the existing bond pattern.
            a. Removal:  Remove  individual  damaged  bricks  with  hammer  and  chisel  without  causing  damage  to  the  
            adjacent brickwork in good condition.  
            b. Cleaning: Remove all existing mortar and debris around the removed bricks and in joints in order to lay new 
            brick in new matching mortar.  
            c. Mortar preparation: prepare mortar to match the existing as mentioned in section 1.1.4.3, chapter 1, Lime 
            Work. 
            d. Laying:  Prewet  the  cavity  created  by  removal  of  bricks  and  lay  mortar  followed  by  bricks  to  match  the  
            existing joints and bond pattern. 
            e. Pointing: After the bricks are laid, pointing or plastering as required should be done to match the existing."""
    )
    kg.create_relationship(subsection_id, "HAS_SUBSUBSECTION", subsubsection_id)

    # 2.5.6.2 Replacing Large Sections
    subsubsection_id = kg.create_subsubsection(
        "2.5.6.2 Replacing Large Sections",
        """
        Replacements should be either new matching brick or matching salvaged brick placed so as to replicate the existing 
        bond pattern.
            a. Supporting the structure: Necessary provision for shoring should be provided to support the adjacent brick 
            work,  around  the  deteriorated  area  to  be  repaired  as  suggested  by  the  conservation  architect  and  the  
            engineer-in-charge.
            b. Dismantling  deteriorated  brickwork:  Deteriorated  bricks  should  be  carefully  removed  by  hand  using  a  
            hammer and chisel. Rebuild back-up and substrate as required to replace any unsound material that was 
            removed. 
            c. Cleaning: Clean the cavity of loose mortar and other debris by hand using a chisel and stiff bristle brushes.
            d. Wetting: Lightly wet the exposed brick surfaces in the cavity created. 
            e. Laying: Lay brick units with matching mortar; butter ends with sufficient mortar to fill joints and insert into place. 
            Each course should match the existing adjacent brickwork courses and patterns. Blend new work into existing 
            work smoothly with no lines of demarcation and no change of pattern or coursing. 
            f. Cleaning: After mortar is thoroughly set and cured, remove loose mortar and dirt from new masonry surfaces. 
            Wash down the masonry surface with clean, clear water.
            g. In case of exposed brickwork, rake all joints in replacement work to receive pointing. Brush all excess mortar 
            from  the  wall  surface  frequently  during  the  work;  protect  all  existing  surfaces  from  mortar  dripping  and  
            splashing. For brick work that was plastered,  should be provided with new palster to to match the existing 
            surfaces after the laying is complete."""
    )
    kg.create_relationship(subsection_id, "HAS_SUBSUBSECTION", subsubsection_id)

    # 2.5.7 Joining Old and New
    subsection_id = kg.create_subsection(
        "2.5.7 Joining Old and New",
        """
        In case the height of the bricks of old as well as new work is the same, the old work should be toothed to the full width 
        of the new wall and to the depth of a quarter of brick in alternate courses. In case the height of the bricks is unequal, 
        then the height of each course of new work should be made equal to the height of the old work by adjusting thickness 
        of horizontal mortar joints in the new wall. Where necessary, adjustment should be made equal to thickness of old wall 
        by adjusting the thickness of vertical joints. 
        For joining new cross wall to old main walls, a number of rectangular recesses of width equal to the thickness of cross 
        wall, three courses in height and half a brick in depth should be cut in the main walls. A space of the three courses 
        should be left between two consecutive recesses. The new cross wall should be bonded into the recesses to avoid 
        any settlement. Joining of old brick work with the new brick work should be done in such a way that there should not 
        be any hump or projection at the joint"""
    )        
    kg.create_relationship(section_id, "HAS_SUBSECTION", subsection_id)

    # 2.5.8 Decorative Elements # 2.5.8 Decorative Elements
    subsection_id = kg.create_subsection(
        "2.5.8 Decorative Elements",
        """
        To achieve decorative details in brickwork, such as mouldings, cornices, string courses, traditionally, soft bricks, 
        cut to shape were laid on beds of lime.

        If the elements are dislodged or are loose, then it should be fixed in place as much as possible.

        In case of deteriorated and missing decorative brick elements, repairs should only be carried out in the most 
        pressing circumstances, where it is the only option. Where repairs are essential, a new replacement should be 
        installed to match the existing.

        Repairs should be carried out by removing deteriorated sections of the decorative brickwork carefully and 
        rebuilding it using the same bricks. In case of missing bricks, new custom-made matching bricks should be used 
        when missing appropriate mortar.

        As per IS: 2212-1991, all projecting architectural features, such as plinth projections, string courses, or cornices, 
        should be effectively bonded by tailing into the brickwork to ensure stability. Such architectural features should be 
        set straight and true with the finished joints as far as possible.

        When such features are not to be plastered over, they should be built with bricks that have high durability, 
        resistance to abrasion, and moisture penetration. Bricks specially made to the required shape for this purpose should 
        be used; if possible otherwise, selected bricks rubbed and ground to correct shape and size may be used.

        Sun shades and such projecting features, which depend on the men of brick masonry over them for their stability, 
        should be kept supported until such time the brick masonry above is built and hardened sufficiently.
        """
    )
    kg.create_relationship(section_id, "HAS_SUBSECTION", subsection_id)



