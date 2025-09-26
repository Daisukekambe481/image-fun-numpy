# 🖼️ Image Fun with NumPy – Pipeline Flow

```text
┌─────────────┐
│ Input Image │
└─────┬───────┘
      │
      ▼
┌─────────────┐
│  loader.py  │
│ Load  &     │ 
│    Inspect  │ 
└─────┬───────┘
      │
      ▼
┌─────────────────────┐
│ transformations.py  │
│ Flip / Rotate       │
└─────┬───────────────┘
      │
      ▼
┌─────────────┐
│ grayscale.py│
│ Convert to  │
│ Grayscale   │
└─────┬───────┘
      │
      ▼
┌─────────────┐
│ color_ops.py│
│ Invert /    │
│ Brighten /  │
│ Channel Ops │
└─────┬───────┘
      │
      ▼
┌─────────────┐
│ filters.py  │
│ Blur / Edge │
│ Sharpen     │
└─────┬───────┘
      │
      ▼
┌─────────────┐
│ effects.py  │
│ Mosaic /    │
│ Noise /     │
│ Glitch      │
└─────┬───────┘
      │
      ▼
┌─────────────┐
│ Output Image│
└─────────────┘
