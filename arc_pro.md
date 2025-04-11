# ArcPy Cheat Sheet

> A quick-reference guide for working with ArcPy in ArcGIS Pro

---

## 📦 Import ArcPy
```python
import arcpy
```

---

## ⚙️ Environment Settings
### How to find Arc Pro Python Interpreter
- In Arc Pro: View > Python Window >
```python
import sys
print(sys.exec_prefix)
```
---
```python
arcpy.env.workspace = r"C:\Path\To\Your\GDB.gdb"
arcpy.env.overwriteOutput = True
```

---

## 📁 Listing Data
```python
arcpy.ListFeatureClasses()
arcpy.ListFields("feature_class")
arcpy.ListDatasets()
arcpy.ListWorkspaces()
```

---

## 🧪 Describe Data
```python
desc = arcpy.Describe("feature_class")
print(desc.shapeType)
print(desc.spatialReference.name)
```

---

## 🔎 SearchCursor (Read rows)
```python
with arcpy.da.SearchCursor("feature_class", ["OID@", "SHAPE@XY"]) as cursor:
    for row in cursor:
        print(row)
```

---

## ✏️ UpdateCursor (Edit rows)
```python
with arcpy.da.UpdateCursor("feature_class", ["Field1"]) as cursor:
    for row in cursor:
        row[0] = "New Value"
        cursor.updateRow(row)
```

---

## ➕ InsertCursor (Add rows)
```python
with arcpy.da.InsertCursor("feature_class", ["Field1", "SHAPE@XY"]) as cursor:
    cursor.insertRow(["New Value", (123.45, 678.90)])
```

---

## 🧰 Common Tools
```python
# Buffer
arcpy.Buffer_analysis("input_fc", "output_fc", "100 Meters")

# Clip
arcpy.Clip_analysis("input_fc", "clip_fc", "output_fc")

# Merge
arcpy.Merge_management(["fc1", "fc2"], "merged_fc")

# Intersect
arcpy.Intersect_analysis(["fc1", "fc2"], "output_fc")

# Dissolve
arcpy.Dissolve_management("input_fc", "output_fc", "FIELD")
```

---

## 🧭 Geometry Handling
```python
# Get centroid of each feature
with arcpy.da.SearchCursor("feature_class", ["OID@", "SHAPE@"], explode_to_points=False) as cursor:
    for oid, shape in cursor:
        print(f"{oid} center: {shape.centroid.X}, {shape.centroid.Y}")

# Get all vertices from polylines
with arcpy.da.SearchCursor("lines_fc", ["SHAPE@"]) as cursor:
    for shape, in cursor:
        for part in shape:
            for point in part:
                if point:
                    print(point.X, point.Y)
```

---

## 🗂 Field Management
```python
# Add a field
arcpy.AddField_management("feature_class", "NewField", "TEXT")

# Calculate field
arcpy.CalculateField_management("feature_class", "NewField", '"Hello"', "PYTHON3")
```

---

## 🔄 Append with Field Mapping
```python
arcpy.Append_management(inputs=["fc1"], target="fc2", schema_type="NO_TEST")
```

---

## 🧼 Clean Up Temp Data
```python
if arcpy.Exists("temp_output"):
    arcpy.Delete_management("temp_output")
```

---

## 🧪 Check Geometry
```python
arcpy.CheckGeometry_management("feature_class", "geometry_issues_table")
```

---

## ❓ Help and Documentation
```python
help(arcpy.Buffer_analysis)
print(arcpy.Buffer_analysis.__doc__)
```

---

## ✅ Best Practices
- Use `with` blocks for cursors
- Always set `arcpy.env.overwriteOutput = True`
- Wrap tools in `try/except` for error handling
- Use `print(arcpy.GetMessages())` to debug tool messages

---

Let me know if you want a version tailored for ArcMap (Python 2) or extra tips for working with rasters, spatial joins, or model builder conversions!

