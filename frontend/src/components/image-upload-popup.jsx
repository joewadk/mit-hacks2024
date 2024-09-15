"use client"

import { useState } from "react"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Button } from "@/components/ui/button"
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription, DialogTrigger } from "@/components/ui/dialog"
import { Upload, Camera, ImagePlus } from "lucide-react";

export function ImageUploadPopup() {
  const [uploadedImage, setUploadedImage] = useState(null)
  const [capturedImage, setCapturedImage] = useState(null)
  const [isOpen, setIsOpen] = useState(false)

  const handleFileUpload = (event) => {
    const file = event.target.files?.[0]
    if (file) {
      const reader = new FileReader()
      reader.onload = (e) => setUploadedImage(e.target?.result)
      reader.readAsDataURL(file)
    }
  }

  const handleCapture = (event) => {
    const file = event.target.files?.[0]
    if (file) {
      const reader = new FileReader()
      reader.onload = (e) => setCapturedImage(e.target?.result)
      reader.readAsDataURL(file)
    }
  }

  const handleSubmit = () => {
    // Handle form submission here
    setIsOpen(false)
  }

  return (
    (<Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DialogTrigger asChild>
        <Button className="flex items-center space-x-2">
          <ImagePlus className="w-4 h-4" />
          <span>Add Image or Details</span>
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px] md:max-w-[700px]">
        <DialogHeader>
          <DialogTitle>Image Upload or Manual Entry</DialogTitle>
          <DialogDescription>Choose how you want to provide the information</DialogDescription>
        </DialogHeader>
        <Tabs defaultValue="upload" className="w-full">
          <TabsList className="grid w-full grid-cols-3">
            <TabsTrigger value="upload">Upload Image</TabsTrigger>
            <TabsTrigger value="capture">Take Picture</TabsTrigger>
            <TabsTrigger value="manual">Manual Entry</TabsTrigger>
          </TabsList>
          <TabsContent value="upload">
            <div className="flex flex-col items-center space-y-4 pt-4">
              <Label htmlFor="image-upload" className="w-full">
                <div
                  className="flex flex-col items-center justify-center w-full h-64 border-2 border-dashed rounded-lg cursor-pointer hover:bg-gray-50">
                  <Upload className="w-12 h-12 text-gray-400" />
                  <p className="mt-2 text-sm text-gray-500">Click to upload or drag and drop</p>
                </div>
                <Input
                  id="image-upload"
                  type="file"
                  accept="image/*"
                  className="hidden"
                  onChange={handleFileUpload} />
              </Label>
              {uploadedImage && (
                <div className="mt-4">
                  <img
                    src={uploadedImage}
                    alt="Uploaded"
                    className="max-w-full h-auto rounded-lg" />
                </div>
              )}
            </div>
          </TabsContent>
          <TabsContent value="capture">
            <div className="flex flex-col items-center space-y-4 pt-4">
              <Label htmlFor="camera-capture" className="w-full">
                <div
                  className="flex flex-col items-center justify-center w-full h-64 border-2 border-dashed rounded-lg cursor-pointer hover:bg-gray-50">
                  <Camera className="w-12 h-12 text-gray-400" />
                  <p className="mt-2 text-sm text-gray-500">Click to take a picture</p>
                </div>
                <Input
                  id="camera-capture"
                  type="file"
                  accept="image/*"
                  capture="environment"
                  className="hidden"
                  onChange={handleCapture} />
              </Label>
              {capturedImage && (
                <div className="mt-4">
                  <img
                    src={capturedImage}
                    alt="Captured"
                    className="max-w-full h-auto rounded-lg" />
                </div>
              )}
            </div>
          </TabsContent>
          <TabsContent value="manual">
            <form className="space-y-4 pt-4">
              <div className="space-y-2">
                <Label htmlFor="name">Name</Label>
                <Input id="name" placeholder="Enter your name" />
              </div>
              <div className="space-y-2">
                <Label htmlFor="email">Email</Label>
                <Input id="email" type="email" placeholder="Enter your email" />
              </div>
              <div className="space-y-2">
                <Label htmlFor="description">Description</Label>
                <Input id="description" placeholder="Enter a description" />
              </div>
            </form>
          </TabsContent>
        </Tabs>
        <div className="mt-6">
          <Button className="w-full" onClick={handleSubmit}>Submit</Button>
        </div>
      </DialogContent>
    </Dialog>)
  );
}