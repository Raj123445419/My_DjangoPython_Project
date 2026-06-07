# Responsive Design Guide for Django Project

## Overview

This guide explains how to implement and use the responsive design framework for your Django project across all devices.

## Device Breakpoints

The responsive design is optimized for the following device categories:

### 1. **Mobile Devices** (320px - 576px)
- Smartphones (portrait and landscape)
- Small tablets (portrait)
- Single column layout
- Touch-optimized navigation
- Large touch targets (48px minimum)

**Features:**
- Hamburger menu for navigation
- Full-width cards and forms
- Single column grid
- Touch-friendly buttons

**Test Devices:**
- iPhone SE (375px)
- iPhone 12 (390px)
- iPhone 14 Pro Max (430px)
- Samsung Galaxy S21 (360px)
- Google Pixel 6 (412px)

### 2. **Tablet Devices** (577px - 992px)
- iPad (portrait)
- iPad Air
- Samsung Galaxy Tab
- Larger tablets (landscape)

**Features:**
- Two-column layout
- Visible navigation bar
- Medium-sized cards
- Optimal for reading

**Test Devices:**
- iPad (768px)
- iPad Mini (768px)
- iPad Pro 11" (834px)
- Samsung Galaxy Tab A (800px)

### 3. **Laptop/Desktop** (993px - 1920px)
- Laptops
- Desktop computers
- Standard monitors
- Wide screens

**Features:**
- Three-column layout
- Full horizontal navigation
- Larger content areas
- Multi-column forms

**Test Devices:**
- Laptop 13" (1280px)
- Laptop 15" (1366px)
- Desktop 24" (1920px)
- Ultrawide 29" (2560px)

### 4. **Large Desktop** (1921px - 3839px)
- Large monitors
- Ultrawide displays
- Home office setups

**Features:**
- Four-column layout
- Expanded content areas
- Larger text and buttons

### 5. **TV Screens** (3840px and above)
- 4K televisions
- Ultra-high resolution displays
- Cinematic experience

**Features:**
- Five-column layout
- Oversized text (28px base font)
- Large buttons and controls
- Navigation optimized for remotes

**Test Devices:**
- 4K TV (3840x2160px)
- 8K TV (7680x4320px)

## File Structure

```
my_project/
├── static/
│   ├── css/
│   │   └── responsive.css        # Main responsive stylesheet
│   └── js/
│       └── responsive.js         # Responsive JavaScript utilities
├── templates/
│   ├── base_responsive.html      # Base template with responsive structure
│   └── responsive_home.html      # Example responsive home page
└── RESPONSIVE_DESIGN_GUIDE.md    # This file
```

## How to Use

### 1. **Base Template**

All your templates should extend `base_responsive.html`:

```html
{% extends 'base_responsive.html' %}
{% load static %}

{% block title %}Your Page Title{% endblock %}

{% block content %}
  <!-- Your content here -->
{% endblock %}
```

### 2. **Responsive Grid System**

Use the `.grid` class for responsive layouts:

```html
<div class="grid">
  <div class="card">Item 1</div>
  <div class="card">Item 2</div>
  <div class="card">Item 3</div>
</div>
```

**Grid columns by device:**
- Mobile: 1 column
- Tablet: 2 columns
- Laptop: 3 columns
- Desktop: 3 columns
- TV: 4-5 columns

### 3. **Cards and Content**

Use the `.card` class for content containers:

```html
<div class="card">
  <h3>Card Title</h3>
  <p>Card content goes here</p>
  <button class="btn">Action</button>
</div>
```

Cards automatically scale and adjust spacing based on device size.

### 4. **Forms**

Forms are fully responsive:

```html
<form method="POST">
  {% csrf_token %}
  <input type="text" placeholder="Name">
  <textarea placeholder="Message"></textarea>
  <button class="btn" type="submit">Submit</button>
</form>
```

**Features:**
- Full-width on mobile
- Constrained width on desktop
- Large tap targets on touch devices
- Accessible labels and error messages

### 5. **Images**

Images are automatically responsive:

```html
<img src="image.jpg" alt="Description">
```

**Features:**
- Scale to container width
- Maintain aspect ratio
- Lazy loading on supported browsers

### 6. **Navigation**

The header includes responsive navigation:
- Hamburger menu on mobile (< 577px)
- Horizontal menu on tablet and larger
- Automatically switches based on screen size

## Custom Responsive Styles

### Adding Media Queries

Follow this pattern for custom responsive styles:

```css
/* Mobile First (default) */
.my-element {
  font-size: 14px;
  padding: 10px;
}

/* Tablet (577px+) */
@media (min-width: 577px) {
  .my-element {
    font-size: 16px;
    padding: 20px;
  }
}

/* Laptop (993px+) */
@media (min-width: 993px) {
  .my-element {
    font-size: 18px;
    padding: 30px;
  }
}

/* TV (3840px+) */
@media (min-width: 3840px) {
  .my-element {
    font-size: 28px;
    padding: 50px;
  }
}
```

### Breakpoint Variables (in your CSS)

```css
/* Mobile: 320px - 576px (default) */
/* Tablet: 577px - 992px */
/* Laptop: 993px - 1920px */
/* Desktop: 1921px - 3839px */
/* TV: 3840px+ */
```

### Utility Classes

**Display Utilities:**
- `.hidden-mobile` - Hide on mobile
- `.hidden-tablet` - Hide on tablet
- `.hidden-desktop` - Hide on laptop/desktop

**Spacing Utilities:**
- `.mt-1`, `.mt-2`, `.mt-3` - Margin top
- `.mb-1`, `.mb-2`, `.mb-3` - Margin bottom

**Text Utilities:**
- `.text-center` - Center align text
- `.text-right` - Right align text

## JavaScript Utilities

The `responsive.js` file provides helpful utilities:

### Get Device Type

```javascript
const deviceType = window.getDeviceType();
// Returns: 'mobile', 'tablet', 'laptop', 'desktop', or 'tv'
```

### Get Viewport Dimensions

```javascript
const viewport = window.getViewport();
// Returns: { width: 1920, height: 1080 }
```

### Device Detection

```javascript
// Check if device is touch-enabled
if (document.body.classList.contains('touch-device')) {
  // Apply touch-specific functionality
}
```

## Testing Responsive Design

### Browser DevTools

1. **Chrome/Edge:**
   - Press `F12` → Click device toolbar (Ctrl+Shift+M)
   - Test with predefined devices or custom sizes

2. **Firefox:**
   - Press `F12` → Click responsive design mode (Ctrl+Shift+M)
   - Test various device profiles

### Manual Testing

Test on actual devices:
- **Mobile:** iPhone, Samsung Galaxy, Google Pixel
- **Tablet:** iPad, Samsung Galaxy Tab
- **Desktop:** Laptop, Desktop with various monitor sizes
- **TV:** Smart TV or large monitor (simulate with CSS)

### Test All Breakpoints

| Device | Width | Breakpoint |
|--------|-------|------------|
| iPhone SE | 375px | Mobile |
| iPhone 14 | 390px | Mobile |
| iPad | 768px | Tablet |
| iPad Air | 820px | Tablet |
| Laptop 13" | 1280px | Laptop |
| Laptop 15" | 1366px | Laptop |
| Desktop 24" | 1920px | Desktop |
| TV 55" 4K | 3840px | TV |

## Performance Optimization

### Image Optimization

```html
<!-- Lazy load images -->
<img data-src="image.jpg" alt="Description">

<!-- Or use native lazy loading -->
<img src="image.jpg" alt="Description" loading="lazy">
```

### Mobile-First CSS

The framework uses mobile-first approach:
- Base styles are for mobile
- Add features for larger screens
- Reduces file size for mobile users
- Better performance

### Responsive Typography

Text scales responsively:
- Mobile: 16px base font
- Tablet: 17px base font
- Laptop: 18px base font
- Desktop: 20px base font
- TV: 28px base font

## Accessibility

### WCAG 2.1 Compliance

- Semantic HTML structure
- ARIA labels for screen readers
- Touch targets ≥ 48px × 48px
- Color contrast ratios ≥ 4.5:1
- Keyboard navigation support

### Touch Accessibility

The framework automatically:
- Increases button sizes on touch devices
- Enables hover effects
- Optimizes for finger interaction

### Motion Preferences

Respects user preferences:
```css
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.01ms !important; }
}
```

## Dark Mode Support

The design includes dark mode support:
- Automatically detects system preference
- Adjusts colors for better visibility
- Preserves contrast ratios

## Browser Support

Supported browsers:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Common Issues & Solutions

### Issue: Content looks cramped on mobile
**Solution:** Increase padding with `.mt-2`, `.mb-2` utility classes

### Issue: Images don't scale
**Solution:** Ensure images have `max-width: 100%` in CSS

### Issue: Navigation menu overlaps content
**Solution:** Check hamburger toggle in `responsive.js`

### Issue: Forms are too wide on mobile
**Solution:** Use `max-width: 400px` on form elements

## Best Practices

1. **Test on real devices** - Emulators can miss edge cases
2. **Use mobile-first approach** - Start with mobile, enhance for larger screens
3. **Optimize images** - Use appropriate image sizes for each device
4. **Minimize HTTP requests** - Combine files, use CSS sprites
5. **Enable lazy loading** - Load images only when needed
6. **Test touch interactions** - Ensure buttons are easily tappable
7. **Check performance** - Use Lighthouse for audits
8. **Validate HTML** - Ensure semantic structure
9. **Test keyboard navigation** - Ensure full accessibility
10. **Monitor device trends** - Add new breakpoints as needed

## Additional Resources

- [MDN Web Docs - Responsive Design](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design)
- [W3C Mobile Web Best Practices](https://www.w3.org/TR/mobile-bp/)
- [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)
- [Lighthouse Performance Audit](https://developers.google.com/web/tools/lighthouse)

## Support

For issues or questions about responsive design:
1. Check browser console for errors
2. Test on multiple devices
3. Review media queries for typos
4. Check viewport meta tag is present
5. Validate CSS syntax

## Updates & Maintenance

- Check for device size trends
- Update breakpoints as needed
- Monitor browser support changes
- Test new devices as they release
- Keep dependencies updated

---

**Last Updated:** 2026
**Responsive Design Framework Version:** 1.0
